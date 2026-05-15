from config import (
    MIN_FVG_SCORE
)


# =========================================
# FVG QUALITY SCORE
# =========================================

def calculate_fvg_score(

    signal,

    current_price,

    current_ema,

    current_atr,

    volume_ratio
):

    try:

        score = 0

        # =========================================
        # EMA TREND
        # =========================================

        if signal['type'] == 'bullish':

            if current_price > current_ema:

                score += 2

        else:

            if current_price < current_ema:

                score += 2

        # =========================================
        # ATR SIZE
        # =========================================

        gap_size = abs(

            signal['gap_high']
            -
            signal['gap_low']
        )

        if gap_size > (

            current_atr * 0.5
        ):

            score += 2

        # =========================================
        # VOLUME
        # =========================================

        if volume_ratio >= 1.5:

            score += 2

        # =========================================
        # STRONG DISPLACEMENT
        # =========================================

        candle_size = abs(

            signal['high']
            -
            signal['low']
        )

        if candle_size > current_atr:

            score += 2

        # =========================================
        # MARKET STRUCTURE BONUS
        # =========================================

        score += 1

        print(
            f'FVG SCORE: {score}'
        )

        return (

            score >= MIN_FVG_SCORE,

            score
        )

    except Exception as e:

        print(e)

        return False, 0