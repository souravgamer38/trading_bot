# =========================================
# LIQUIDITY SWEEP
# =========================================

def detect_liquidity_sweep(
    df
):

    try:

        recent_high = max(
            df['high'].iloc[-10:-1]
        )

        recent_low = min(
            df['low'].iloc[-10:-1]
        )

        current_high = (
            df['high'].iloc[-1]
        )

        current_low = (
            df['low'].iloc[-1]
        )

        current_close = (
            df['close'].iloc[-1]
        )

        # =========================================
        # BUY SIDE LIQUIDITY SWEEP
        # =========================================

        if (

            current_high > recent_high

            and

            current_close < recent_high
        ):

            return 'bearish'

        # =========================================
        # SELL SIDE LIQUIDITY SWEEP
        # =========================================

        elif (

            current_low < recent_low

            and

            current_close > recent_low
        ):

            return 'bullish'

        return None

    except Exception as e:

        print(e)

        return None