from config import (

    MAX_LOT_SIZE,

    HIGH_VOLATILITY_THRESHOLD,

    MEDIUM_VOLATILITY_THRESHOLD
)


# =========================================
# VOLATILITY POSITION SIZE
# =========================================

def volatility_position_size(

    base_qty,

    atr,

    current_price
):

    try:

        volatility_ratio = (
            atr / current_price
        )

        # =========================================
        # HIGH VOLATILITY
        # =========================================

        if (

            volatility_ratio
            >=
            HIGH_VOLATILITY_THRESHOLD
        ):

            adjusted_qty = (
                base_qty * 0.50
            )

        # =========================================
        # MEDIUM VOLATILITY
        # =========================================

        elif (

            volatility_ratio
            >=
            MEDIUM_VOLATILITY_THRESHOLD
        ):

            adjusted_qty = (
                base_qty * 0.75
            )

        # =========================================
        # LOW VOLATILITY
        # =========================================

        else:

            adjusted_qty = (
                base_qty
            )

        # =========================================
        # MAX LOT SIZE
        # =========================================

        if adjusted_qty > MAX_LOT_SIZE:

            adjusted_qty = MAX_LOT_SIZE

        return round(
            adjusted_qty,
            2
        )

    except Exception as e:

        print(e)

        return base_qty
