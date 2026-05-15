from config import (
    EMA_PERIOD
)


# =========================================
# TREND FILTER
# =========================================

def trend_filter(

    current_price,

    ema
):

    try:

        # =========================================
        # ABOVE EMA
        # =========================================

        if current_price > ema:

            return True

        # =========================================
        # BELOW EMA
        # =========================================

        elif current_price < ema:

            return True

        return False

    except Exception as e:

        print(e)

        return False


# =========================================
# VOLATILITY FILTER
# =========================================

def volatility_filter(
    atr
):

    try:

        # =========================================
        # LOW VOLATILITY
        # =========================================

        if atr <= 0:

            return False

        return True

    except Exception as e:

        print(e)

        return False