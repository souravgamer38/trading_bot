from config import (
    MIN_DISPLACEMENT_RATIO
)


# =========================================
# DISPLACEMENT FILTER
# =========================================

def displacement_ok(

    signal,

    atr
):

    try:

        candle_size = abs(

            signal['high']
            -
            signal['low']
        )

        ratio = (
            candle_size / atr
        )

        print(
            f'DISPLACEMENT RATIO: {ratio}'
        )

        return (
            ratio
            >=
            MIN_DISPLACEMENT_RATIO
        )

    except Exception as e:

        print(e)

        return False