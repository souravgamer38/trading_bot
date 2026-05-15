import requests

from config import (

    ENABLE_TELEGRAM,

    TELEGRAM_BOT_TOKEN,

    TELEGRAM_CHAT_ID
)


# =========================================
# SEND TELEGRAM MESSAGE
# =========================================

def send_telegram(
    message
):

    try:

        # =========================================
        # FEATURE DISABLED
        # =========================================

        if not ENABLE_TELEGRAM:

            return

        url = f'''

https://api.telegram.org/bot

{TELEGRAM_BOT_TOKEN}

/sendMessage

'''

        payload = {

            'chat_id': TELEGRAM_CHAT_ID,

            'text': message
        }

        response = requests.post(

            url.strip(),

            data=payload
        )

        # =========================================
        # DEBUG
        # =========================================

        print(
            'TELEGRAM MESSAGE SENT'
        )

        return response.json()

    except Exception as e:

        print(e)

        return None


# =========================================
# SEND PHOTO
# =========================================

def send_photo(

    photo_path,

    caption=''
):

    try:

        # =========================================
        # FEATURE DISABLED
        # =========================================

        if not ENABLE_TELEGRAM:

            return

        url = f'''

https://api.telegram.org/bot

{TELEGRAM_BOT_TOKEN}

/sendPhoto

'''

        with open(
            photo_path,
            'rb'
        ) as photo:

            response = requests.post(

                url.strip(),

                data={

                    'chat_id': TELEGRAM_CHAT_ID,

                    'caption': caption
                },

                files={

                    'photo': photo
                }
            )

        print(
            'PHOTO SENT'
        )

        return response.json()

    except Exception as e:

        print(e)

        return None


# =========================================
# SEND ERROR
# =========================================

def send_error(
    error_message
):

    try:

        message = f'''

❌ BOT ERROR

{error_message}
'''

        send_telegram(
            message
        )

    except Exception as e:

        print(e)


# =========================================
# SEND TRADE ALERT
# =========================================

def send_trade_alert(

    symbol,

    side,

    entry,

    sl,

    tp
):

    try:

        message = f'''

🚀 NEW TRADE

PAIR:
{symbol}

SIDE:
{side}

ENTRY:
{entry}

SL:
{sl}

TP:
{tp}
'''

        send_telegram(
            message
        )

    except Exception as e:

        print(e)


# =========================================
# SEND STARTUP MESSAGE
# =========================================

def send_startup():

    try:

        send_telegram(
            '🤖 BOT STARTED'
        )

    except Exception as e:

        print(e)


# =========================================
# SEND SHUTDOWN MESSAGE
# =========================================

def send_shutdown():

    try:

        send_telegram(
            '🛑 BOT STOPPED'
        )

    except Exception as e:

        print(e)