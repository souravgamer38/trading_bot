from config import (
    MAX_LOT_SIZE
)


# =========================================
# POSITION SIZE CALCULATION
# =========================================

def calculate_position(

    usd_balance,

    risk_percent,

    entry,

    sl
):

    try:

        risk_amount = (

            usd_balance
            *
            risk_percent
        ) / 100

        sl_distance = abs(
            entry - sl
        )

        if sl_distance <= 0:

            return 0

        qty = (
            risk_amount
            /
            sl_distance
        )

        # =========================================
        # MAX LOT LIMIT
        # =========================================

        if qty > MAX_LOT_SIZE:

            qty = MAX_LOT_SIZE

        return round(
            qty,
            2
        )

    except Exception as e:

        print(e)

        return 0