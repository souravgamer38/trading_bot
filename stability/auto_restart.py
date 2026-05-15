import os
import time

from telegram.telegram_bot import (
    send_telegram
)


# =========================================
# AUTO RESTART
# =========================================

def auto_restart():

    try:

        print(
            'AUTO RESTART STARTED'
        )

        send_telegram(
            '♻️ BOT RESTARTING'
        )

        time.sleep(5)

        os.system(
            'python main.py'
        )

    except Exception as e:

        print(e)