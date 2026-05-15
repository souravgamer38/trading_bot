import ccxt

from config import (

    API_KEY,

    API_SECRET,

    DEBUG_MODE
)


# =========================================
# CREATE EXCHANGE
# =========================================

def create_exchange():

    try:

        exchange = ccxt.delta({

            'apiKey': API_KEY,

            'secret': API_SECRET,

            'enableRateLimit': True
        })

        exchange.load_markets()

        if DEBUG_MODE:

            print(
                'EXCHANGE CONNECTED'
            )

        return exchange

    except Exception as e:

        print(e)

        return None


# =========================================
# CHECK CONNECTION
# =========================================

def connection_ok(
    exchange
):

    try:

        exchange.fetch_ticker(
            'ETHUSDT'
        )

        return True

    except Exception as e:

        print(e)

        return False