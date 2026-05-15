from datetime import datetime


# =========================================
# CANDLE CLOSE CONFIRMATION
# =========================================

def candle_closed(
    timeframe
):

    now = datetime.utcnow()

    minute = now.minute

    # =========================================
    # 1 MIN
    # =========================================

    if timeframe == '1m':

        return now.second >= 55

    # =========================================
    # 5 MIN
    # =========================================

    elif timeframe == '5m':

        return (

            minute % 5 == 0

            and

            now.second >= 55
        )

    # =========================================
    # 15 MIN
    # =========================================

    elif timeframe == '15m':

        return (

            minute % 15 == 0

            and

            now.second >= 55
        )

    # =========================================
    # 1 HOUR
    # =========================================

    elif timeframe == '1h':

        return (

            minute == 0

            and

            now.second >= 55
        )

    return False