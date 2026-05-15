# =========================================
# MARKET STRUCTURE
# =========================================

def detect_market_structure(
    df
):

    try:

        recent_highs = (
            df['high'].iloc[-5:]
        )

        recent_lows = (
            df['low'].iloc[-5:]
        )

        # =========================================
        # BULLISH
        # =========================================

        if (

            recent_highs.is_monotonic_increasing

            and

            recent_lows.is_monotonic_increasing
        ):

            return 'bullish'

        # =========================================
        # BEARISH
        # =========================================

        elif (

            recent_highs.is_monotonic_decreasing

            and

            recent_lows.is_monotonic_decreasing
        ):

            return 'bearish'

        return 'range'

    except Exception as e:

        print(e)

        return 'range'