import time

from config import (
    TRADING_MODE,

    ATR_TRAILING_MULTIPLIER
)

from telegram.telegram_bot import (
    send_telegram
)

from storage.state_manager import (
    clear_active_trade
)

from stability.trade_registry import (
    clear_active_trade as clear_registry
)

from analytics.logger import (
    log_trade
)

from storage.database import (
    save_trade_db
)


# =========================================
# MANAGE TRADE
# =========================================

def manage_trade(

    exchange,

    symbol,

    side,

    entry,

    sl,

    tp,

    qty,

    sl_order_id
):

    try:

        print(
            'WATCHDOG STARTED'
        )

        trailing_sl = sl

        while True:

            # =========================================
            # PAPER MODE PRICE
            # =========================================

            if TRADING_MODE == 'PAPER':

                ticker = exchange.fetch_ticker(
                    symbol
                )

                current_price = ticker[
                    'last'
                ]

            # =========================================
            # LIVE MODE PRICE
            # =========================================

            else:

                ticker = exchange.fetch_ticker(
                    symbol
                )

                current_price = ticker[
                    'last'
                ]

            # =========================================
            # BUY TRADE
            # =========================================

            if side == 'bullish':

                # =========================================
                # TRAILING STOP
                # =========================================

                new_sl = (

                    current_price
                    -
                    ATR_TRAILING_MULTIPLIER
                )

                if new_sl > trailing_sl:

                    trailing_sl = new_sl

                # =========================================
                # TAKE PROFIT
                # =========================================

                if current_price >= tp:

                    pnl = (
                        abs(tp - entry)
                        * qty
                    )

                    close_trade(

                        symbol,

                        side,

                        entry,

                        tp,

                        qty,

                        pnl,

                        'TP'
                    )

                    break

                # =========================================
                # STOPLOSS
                # =========================================

                elif current_price <= trailing_sl:

                    pnl = -(
                        abs(entry - trailing_sl)
                        * qty
                    )

                    close_trade(

                        symbol,

                        side,

                        entry,

                        trailing_sl,

                        qty,

                        pnl,

                        'SL'
                    )

                    break

            # =========================================
            # SELL TRADE
            # =========================================

            else:

                # =========================================
                # TRAILING STOP
                # =========================================

                new_sl = (

                    current_price
                    +
                    ATR_TRAILING_MULTIPLIER
                )

                if new_sl < trailing_sl:

                    trailing_sl = new_sl

                # =========================================
                # TAKE PROFIT
                # =========================================

                if current_price <= tp:

                    pnl = (
                        abs(entry - tp)
                        * qty
                    )

                    close_trade(

                        symbol,

                        side,

                        entry,

                        tp,

                        qty,

                        pnl,

                        'TP'
                    )

                    break

                # =========================================
                # STOPLOSS
                # =========================================

                elif current_price >= trailing_sl:

                    pnl = -(
                        abs(trailing_sl - entry)
                        * qty
                    )

                    close_trade(

                        symbol,

                        side,

                        entry,

                        trailing_sl,

                        qty,

                        pnl,

                        'SL'
                    )

                    break

            time.sleep(2)

    except Exception as e:

        print(e)


# =========================================
# CLOSE TRADE
# =========================================

def close_trade(

    symbol,

    side,

    entry,

    exit_price,

    qty,

    pnl,

    result
):

    try:

        send_telegram(
f'''
📊 TRADE CLOSED

Pair:
{symbol}

Side:
{side}

Result:
{result}

PnL:
{round(pnl, 2)}
'''
        )

        # =========================================
        # DATABASE
        # =========================================

        save_trade_db(

            symbol=symbol,

            side=side,

            entry=entry,

            sl=0,

            tp=0,

            qty=qty,

            rr=0,

            pnl=pnl,

            result=result,

            fvg_score=0
        )

        # =========================================
        # LOGGER
        # =========================================

        log_trade({

            'mode': TRADING_MODE,

            'symbol': symbol,

            'side': side,

            'entry': entry,

            'sl': 0,

            'tp': exit_price,

            'qty': qty,

            'rr': 0,

            'result': result,

            'pnl': pnl,

            'fvg_score': 0
        })

        # =========================================
        # CLEAR STATES
        # =========================================

        clear_active_trade()

        clear_registry()

        print(
            'TRADE CLOSED'
        )

    except Exception as e:

        print(e)
