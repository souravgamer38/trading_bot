import signal
import sys

from telegram.telegram_bot import (
    send_telegram
)


# =========================================
# SHUTDOWN HANDLER
# =========================================

def graceful_shutdown(

    signum,

    frame
):

    try:

        print(
            'GRACEFUL SHUTDOWN'
        )

        send_telegram(
            '🛑 BOT SHUTDOWN'
        )

        sys.exit(0)

    except Exception as e:

        print(e)


# =========================================
# REGISTER
# =========================================

def register_shutdown():

    signal.signal(

        signal.SIGINT,

        graceful_shutdown
    )

    signal.signal(

        signal.SIGTERM,

        graceful_shutdown
    )