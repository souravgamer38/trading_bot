import time

from analytics.logger import log_info

from config import (
    TRADING_MODE
)

from telegram.telegram_bot import (
    send_telegram
)


# =========================================
# PAPER TRADE
# =========================================

def paper_trade(

    signal,

    symbol,

    qty,

    entry,

    sl,

    tp
):

    log_info("PAPER TRADE")

    return {

        'mode': 'PAPER',

        'symbol': symbol,

        'side': signal[
            'type'
        ],

        'entry': entry,

        'sl': sl,

        'tp': tp,

        'qty': qty,

        'status': 'FILLED',

        'sl_order': {

            'id': 'paper_sl'
        }
    }


# =========================================
# LIVE TRADE
# =========================================

def live_trade(

    exchange,

    signal,

    symbol,

    qty,

    entry,

    sl,

    tp
):

    try:

        side = signal[
            'type'
        ]

        # =========================================
        # BUY
        # =========================================

        if side == 'bullish':

            order = exchange.create_market_buy_order(

                symbol,

                qty
            )

        # =========================================
        # SELL
        # =========================================

        else:

            order = exchange.create_market_sell_order(

                symbol,

                qty
            )

        time.sleep(1)

        sl_order = {

            'id': f'sl_{time.time()}'
        }

        send_telegram(
f'''
🚀 LIVE ORDER EXECUTED

Pair:
{symbol}

Side:
{side}

Qty:
{qty}
'''
        )

        return {

            'mode': 'LIVE',

            'symbol': symbol,

            'side': side,

            'entry': entry,

            'sl': sl,

            'tp': tp,

            'qty': qty,

            'status': 'FILLED',

            'order': order,

            'sl_order': sl_order
        }

    except Exception as e:

        print(e)

        return None


# =========================================
# PLACE TRADE
# =========================================

def place_trade(

    exchange,

    signal,

    symbol,

    qty,

    entry,

    sl,

    tp
):

    # =========================================
    # PAPER MODE
    # =========================================

    if TRADING_MODE == 'PAPER':

        return paper_trade(

            signal,

            symbol,

            qty,

            entry,

            sl,

            tp
        )

    # =========================================
    # LIVE MODE
    # =========================================

    elif TRADING_MODE == 'LIVE':

        return live_trade(

            exchange,

            signal,

            symbol,

            qty,

            entry,

            sl,

            tp
        )

    return None
