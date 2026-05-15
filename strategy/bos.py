# =========================================
# BREAK OF STRUCTURE
# =========================================

def detect_bos(
    df
):

    try:

        recent_high = max(
            df['high'].iloc[-6:-1]
        )

        recent_low = min(
            df['low'].iloc[-6:-1]
        )

        current_close = (
            df['close'].iloc[-1]
        )

        # =========================================
        # BULLISH BOS
        # =========================================

        if current_close > recent_high:

            return 'bullish'

        # =========================================
        # BEARISH BOS
        # =========================================

        elif current_close < recent_low:

            return 'bearish'

        return None

    except Exception as e:

        print(e)

        return None