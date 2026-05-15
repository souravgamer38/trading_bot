import time

from telegram.telegram_bot import (
    send_telegram
)


# =========================================
# RECONNECT EXCHANGE
# =========================================

def reconnect_exchange(
    exchange
):

    try:

        print(
            'RECONNECTING EXCHANGE'
        )

        send_telegram(
            '🔄 RECONNECTING EXCHANGE'
        )

        time.sleep(5)

        exchange.load_markets()

        print(
            'RECONNECTED'
        )

        send_telegram(
            '✅ EXCHANGE RECONNECTED'
        )

        return True

    except Exception as e:

        print(e)

        send_telegram(
            '❌ RECONNECT FAILED'
        )

        return False