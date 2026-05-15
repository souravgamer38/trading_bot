# =========================================
# CHOCH DETECTION
# =========================================

def detect_choch(
    df
):

    try:

        prev_high = max(
            df['high'].iloc[-10:-5]
        )

        recent_high = max(
            df['high'].iloc[-5:]
        )

        prev_low = min(
            df['low'].iloc[-10:-5]
        )

        recent_low = min(
            df['low'].iloc[-5:]
        )

        # =========================================
        # BULLISH CHOCH
        # =========================================

        if recent_high > prev_high:

            return 'bullish'

        # =========================================
        # BEARISH CHOCH
        # =========================================

        elif recent_low < prev_low:

            return 'bearish'

        return None

    except Exception as e:

        print(e)

        return None