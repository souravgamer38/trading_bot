from config import (
    MIN_VOLUME_RATIO
)


# =========================================
# VOLUME FILTER
# =========================================

def volume_ok(
    df
):

    try:

        current_volume = (
            df['volume']
            .iloc[-1]
        )

        average_volume = (

            df['volume']

            .rolling(20)

            .mean()

            .iloc[-1]
        )

        if average_volume <= 0:

            return False

        volume_ratio = (
            current_volume
            /
            average_volume
        )

        print(
            f'VOLUME RATIO: {volume_ratio}'
        )

        return (
            volume_ratio
            >=
            MIN_VOLUME_RATIO
        )

    except Exception as e:

        print(e)

        return False