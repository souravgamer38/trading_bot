from config import (
    MIN_IMBALANCE_ATR_RATIO
)


# =========================================
# IMBALANCE FILTER
# =========================================

def imbalance_ok(

    signal,

    atr
):

    try:

        imbalance_size = abs(

            signal['gap_high']
            -
            signal['gap_low']
        )

        ratio = (
            imbalance_size / atr
        )

        print(
            f'IMBALANCE RATIO: {ratio}'
        )

        return (
            ratio
            >=
            MIN_IMBALANCE_ATR_RATIO
        )

    except Exception as e:

        print(e)

        return False