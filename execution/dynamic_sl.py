from config import (
    ATR_SL_MULTIPLIER
)


# =========================================
# DYNAMIC STOPLOSS
# =========================================

def dynamic_stoploss(

    signal_type,

    current_price,

    atr
):

    try:

        sl_distance = (
            atr
            *
            ATR_SL_MULTIPLIER
        )

        # =========================================
        # BUY
        # =========================================

        if signal_type == 'bullish':

            sl = (
                current_price
                -
                sl_distance
            )

        # =========================================
        # SELL
        # =========================================

        else:

            sl = (
                current_price
                +
                sl_distance
            )

        return round(
            sl,
            2
        )

    except Exception as e:

        print(e)

        return current_price
