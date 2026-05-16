import time
import threading
import pandas as pd
import signal
import sys

from ta.trend import EMAIndicator
from ta.volatility import AverageTrueRange

from config import *

from analytics.logger import (
    current_time
)

from utils.api_manager import (
    create_exchange
)

from utils.config_validator import (
    validate_config
)

from utils.signal_tracker import (
    is_new_signal
)

from strategy.strategy import (
    detect_fvg
)

from strategy.fvg_score import (
    calculate_fvg_score
)

from strategy.displacement_filter import (
    displacement_ok
)

from strategy.imbalance_filter import (
    imbalance_ok
)

from strategy.market_structure import (
    detect_market_structure
)

from strategy.bos import (
    detect_bos
)

from strategy.choch import (
    detect_choch
)

from strategy.order_block import (
    detect_order_block
)

from strategy.liquidity_sweep import (
    detect_liquidity_sweep
)

from execution.execute import (
    place_trade
)

from execution.watchdog import (
    manage_trade
)

from execution.dynamic_sl import (
    dynamic_stoploss
)

from execution.dynamic_rr import (
    dynamic_rr
)

from execution.volatility_position import (
    volatility_position_size
)

from risk.risk import (
    calculate_position
)

from risk.risk_guard import (
    max_loss_reached
)

from risk.portfolio_risk import (
    exposure_ok
)

from risk.correlation_filter import (
    correlation_ok
)

from filters.filters import (
    trend_filter,
    volatility_filter
)

from filters.volume_filter import (
    volume_ok
)

from filters.spread_filter import (
    spread_ok
)

from filters.liquidity_filter import (
    liquidity_ok
)

from filters.candle_confirm import (
    candle_closed
)

from filters.sessions import (
    smart_session
)

from filters.news_filter import (
    news_safe
)

from storage.database import (
    initialize_database
)

from storage.state_manager import (

    load_state,

    update_state,

    save_active_trade,

    clear_active_trade
)

from stability.thread_lock import (
    trade_lock
)

from stability.trade_registry import (

    set_active_trade,

    clear_active_trade as clear_registry,

    has_active_trade
)

from stability.rate_limit import (
    rate_limiter
)

from stability.reconnect import (
    reconnect_exchange
)

from stability.shutdown_handler import (
    register_shutdown
)

from analytics.performance_report import (
    generate_report
)

from analytics.periodic_reports import (
    send_periodic_reports
)

from analytics.logger import (

    log_info,

    log_error
)

from telegram.telegram_bot import (

    send_telegram,

    send_startup,
    
    send_shutdown
)


# =========================================
# CONFIG VALIDATION
# =========================================

if not validate_config():

    quit()


# =========================================
# STARTUP
# =========================================

send_startup()

register_shutdown()

initialize_database()


# =========================================
# EXCHANGE
# =========================================

exchange = create_exchange()

if exchange is None:

    quit()


# =========================================
# LOAD STATE
# =========================================

state = load_state()

last_trade_time = state.get(
    'last_trade_time',
    0
)


# =========================================
# GET DATA
# =========================================

def get_data():

    try:

        ohlcv = rate_limiter.safe_request(

            exchange.fetch_ohlcv,

            SYMBOL,

            timeframe=TIMEFRAME,

            limit=250
        )

        if ohlcv is None:

            return None

        df = pd.DataFrame(

            ohlcv,

            columns=[

                'time',

                'open',

                'high',

                'low',

                'close',

                'volume'
            ]
        )

        return df

    except Exception as e:

        log_error(str(e))

        return None


# =========================================
# APPLY INDICATORS
# =========================================

def apply_indicators(
    df
):

    ema = EMAIndicator(

        close=df['close'],

        window=EMA_PERIOD
    )

    df['ema'] = (
        ema.ema_indicator()
    )

    atr = AverageTrueRange(

        high=df['high'],

        low=df['low'],

        close=df['close'],

        window=ATR_PERIOD
    )

    df['atr'] = (
        atr.average_true_range()
    )

    return df


# =========================================
# MAIN LOOP
# =========================================

def trading_loop():

    global last_trade_time

    while True:

        try:

            if DEBUG_MODE:
                print(
        f'RUNNING {TRADING_MODE} MODE'
    )

            # =========================================
            # ACTIVE TRADE CHECK
            # =========================================

            if has_active_trade():

                if DEBUG_MODE:
                        print(
        'ACTIVE TRADE EXISTS'
    )

                time.sleep(15)

                continue

            # =========================================
            # SESSION FILTER
            # =========================================

            if not smart_session():

                time.sleep(60)

                continue

            # =========================================
            # NEWS FILTER
            # =========================================

            if ENABLE_NEWS_FILTER:

                if not news_safe():

                    print(
                        'NEWS BLOCKED'
                    )

                    time.sleep(300)

                    continue

            # =========================================
            # DAILY LOSS
            # =========================================

            if max_loss_reached():

                print(
                    'MAX DAILY LOSS HIT'
                )

                time.sleep(300)

                continue

            # =========================================
            # COOLDOWN
            # =========================================

            if (

                time.time()

                -
                last_trade_time

                <
                COOLDOWN_SECONDS
            ):

                print(
                    'COOLDOWN ACTIVE'
                )

                time.sleep(30)

                continue

            # =========================================
            # DATA
            # =========================================

            df = get_data()

            if df is None:

                continue

            df = apply_indicators(
                df
            )

            current_price = (
                df['close'].iloc[-1]
            )

            current_ema = (
                df['ema'].iloc[-1]
            )

            current_atr = (
                df['atr'].iloc[-1]
            )

            # =========================================
            # FILTERS
            # =========================================

            if not trend_filter(

                current_price,

                current_ema
            ):

                continue

            if not volatility_filter(
                current_atr
            ):

                continue

            if not volume_ok(
                df
            ):

                continue

            if not candle_closed(
                TIMEFRAME
            ):

                continue

            if not spread_ok(

                exchange,

                SYMBOL
            ):

                continue

            if not liquidity_ok(

                exchange,

                SYMBOL
            ):

                continue

            # =========================================
            # STRUCTURE
            # =========================================

            market_structure = (
                detect_market_structure(
                    df
                )
            )

            bos = detect_bos(df)

            choch = detect_choch(df)

            order_block = (
                detect_order_block(
                    df
                )
            )

            liquidity_sweep = (
                detect_liquidity_sweep(
                    df
                )
            )

            # =========================================
            # FVG
            # =========================================

            signals = detect_fvg(
                df
            )

            if len(signals) == 0:

                time.sleep(10)

                continue

            signal = signals[-1]

            # =========================================
            # DUPLICATE SIGNAL
            # =========================================

            if not is_new_signal(
                signal['time']
            ):

                continue

            # =========================================
            # FVG SCORE
            # =========================================

            avg_volume = (

                df['volume']

                .rolling(20)

                .mean()

                .iloc[-1]
            )

            volume_ratio = (

                df['volume'].iloc[-1]

                /
                avg_volume
            )

            valid_fvg, fvg_score = (

                calculate_fvg_score(

                    signal,

                    current_price,

                    current_ema,

                    current_atr,

                    volume_ratio
                )
            )

            if not valid_fvg:

                continue

            # =========================================
            # DISPLACEMENT
            # =========================================

            if not displacement_ok(

                signal,

                current_atr
            ):

                continue

            # =========================================
            # IMBALANCE
            # =========================================

            if not imbalance_ok(

                signal,

                current_atr
            ):

                continue

            # =========================================
            # CORRELATION FILTER
            # =========================================

            if not correlation_ok(

                exchange,

                SYMBOL,

                signal['type']
            ):

                continue

            # =========================================
            # STRUCTURE CONFIRMATION
            # =========================================

            if signal['type'] == 'bullish':

                if market_structure != 'bullish':

                    continue

                if bos != 'bullish':

                    continue

                if choch != 'bullish':

                    continue

                if liquidity_sweep != 'bullish':

                    continue

                if order_block['type'] != 'bullish':

                    continue

            else:

                if market_structure != 'bearish':

                    continue

                if bos != 'bearish':

                    continue

                if choch != 'bearish':

                    continue

                if liquidity_sweep != 'bearish':

                    continue

                if order_block['type'] != 'bearish':

                    continue

            # =========================================
            # DYNAMIC SL
            # =========================================

            sl = dynamic_stoploss(

                signal['type'],

                current_price,

                current_atr
            )

            # =========================================
            # BALANCE
            # =========================================

            if TRADING_MODE == 'PAPER':

                usd_balance = (
                    PAPER_BALANCE
                )

            else:

                balance = (

                    rate_limiter.safe_request(
                        exchange.fetch_balance
                    )
                )

                usd_balance = balance[
                    'total'
                ]['USD']

            # =========================================
            # POSITION SIZE
            # =========================================

            base_qty = calculate_position(

                usd_balance,

                RISK_PERCENT,

                current_price,

                sl
            )

            qty = volatility_position_size(

                base_qty,

                current_atr,

                current_price
            )

            # =========================================
            # DYNAMIC RR
            # =========================================

            rr = dynamic_rr(

                current_price,

                current_ema,

                current_atr
            )

            # =========================================
            # TP
            # =========================================

            risk_distance = abs(
                current_price - sl
            )

            if signal['type'] == 'bullish':

                tp = (
                    current_price
                    +
                    (risk_distance * rr)
                )

            else:

                tp = (
                    current_price
                    -
                    (risk_distance * rr)
                )

            # =========================================
            # EXPOSURE
            # =========================================

            trade_value = (
                qty * current_price
            )

            if not exposure_ok(

                exchange,

                SYMBOL,

                usd_balance,

                trade_value
            ):

                continue

            # =========================================
            # EXECUTE
            # =========================================

            with trade_lock:

                trade_data = place_trade(

                    exchange,

                    signal,

                    SYMBOL,

                    qty,

                    current_price,

                    sl,

                    tp
                )

            # =========================================
            # TRADE SUCCESS
            # =========================================

            if trade_data:

                set_active_trade({

                    'symbol': SYMBOL,

                    'side': signal[
                        'type'
                    ],

                    'entry': current_price,

                    'sl': sl,

                    'tp': tp,

                    'qty': qty
                })

                save_active_trade({

                    'symbol': SYMBOL,

                    'side': signal[
                        'type'
                    ],

                    'entry': current_price,

                    'sl': sl,

                    'tp': tp,

                    'qty': qty,

                    'sl_order_id': trade_data[
                        'sl_order'
                    ]['id']
                })

                trade_thread = threading.Thread(

                    target=manage_trade,

                    kwargs={

                        'exchange': exchange,

                        'symbol': SYMBOL,

                        'side': signal[
                            'type'
                        ],

                        'entry': current_price,

                        'sl': sl,

                        'tp': tp,

                        'qty': qty,

                        'sl_order_id': trade_data[
                            'sl_order'
                        ]['id']
                    }
                )

                trade_thread.start()

                last_trade_time = (
                    time.time()
                )

                update_state(

                    'last_trade_time',

                    last_trade_time
                )

                send_telegram(
f'''
🚀 TRADE OPENED

MODE:
{TRADING_MODE}

PAIR:
{SYMBOL}

SIDE:
{signal['type']}

ENTRY:
{current_price}

SL:
{sl}

TP:
{tp}

RR:
{rr}

FVG SCORE:
{fvg_score}
'''
                )

            # =========================================
            # REPORTS
            # =========================================

            print(
                generate_report()
            )

            send_periodic_reports()

            time.sleep(15)

        except Exception as e:

            log_error(str(e))

            reconnect_exchange(
                exchange
            )

            time.sleep(10)


# =========================================
# START BOT
# =========================================

main_thread = threading.Thread(

    target=trading_loop
)

main_thread.start()


startup_message = f'''
╔════════════════════════════╗
      🚀 FVG TRADING BOT 🚀
╚════════════════════════════╝

🟢 STATUS        : RUNNING SUCCESSFULLY
📅 DATE         : {current_time()}
📊 MODE         : {TRADING_MODE}
🧠 STRATEGY     : FVG + SMART MONEY
🛡️ SYSTEM STATUS : ALL MODULES ACTIVE
🔔 TELEGRAM     : CONNECTED
🔒 PROTECTION   : ENABLED

⚡ Bot is now monitoring market...
💰 Waiting for high probability setup

════════════════════════════
'''

startup_message_2 = f'''
╔══════════════════════╗
      🚀 FVG TRADING BOT 🚀
╚══════════════════════╝

🟢 STATUS                : 
RUNNING SUCCESSFULLY

📅 DATE                     : 
{current_time()}

📊 MODE                    : 
{TRADING_MODE}

🧠 STRATEGY            : 
FVG + SMART MONEY

🛡️ SYSTEM STATUS : 
ALL MODULES ACTIVE

🔔 TELEGRAM           : 
CONNECTED

🔒 PROTECTION       : 
ENABLED

⚡ Bot is now monitoring market...
💰 Waiting for high probability setup

════════════════════════
'''

print(startup_message)

log_info(startup_message)

send_telegram(startup_message_2)