from config import (

    MIN_RR,

    MAX_RR
)


# =========================================
# DYNAMIC RR
# =========================================

def dynamic_rr(

    current_price,

    ema,

    atr
):

    try:

        distance = abs(
            current_price - ema
        )

        ratio = (
            distance / atr
        )

        # =========================================
        # STRONG TREND
        # =========================================

        if ratio >= 3:

            rr = MAX_RR

        # =========================================
        # MEDIUM TREND
        # =========================================

        elif ratio >= 2:

            rr = 3

        # =========================================
        # WEAK TREND
        # =========================================

        else:

            rr = MIN_RR

        return round(
            rr,
            2
        )

    except Exception as e:

        print(e)

        return MIN_RR
