from config import (
    MAX_SPREAD_PERCENT
)


# =========================================
# SPREAD FILTER
# =========================================

def spread_ok(

    exchange,

    symbol
):

    try:

        ticker = exchange.fetch_ticker(
            symbol
        )

        bid = ticker[
            'bid'
        ]

        ask = ticker[
            'ask'
        ]

        if bid == 0:

            return False

        spread_percent = (

            (ask - bid)
            /
            bid
        ) * 100

        print(
            f'SPREAD: {spread_percent}'
        )

        return (
            spread_percent
            <=
            MAX_SPREAD_PERCENT
        )

    except Exception as e:

        print(e)

        return False