from analytics.analytics import (
    total_pnl
)

from config import (
    MAX_DAILY_LOSS_PERCENT
)


# =========================================
# DAILY LOSS GUARD
# =========================================

def max_loss_reached():

    try:

        pnl = total_pnl()

        # =========================================
        # MAX LOSS HIT
        # =========================================

        if pnl <= -MAX_DAILY_LOSS_PERCENT:

            print(
                'MAX DAILY LOSS REACHED'
            )

            return True

        return False

    except Exception as e:

        print(e)

        return False