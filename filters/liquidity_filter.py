from config import (
    MIN_ORDERBOOK_VOLUME
)


# =========================================
# LIQUIDITY FILTER
# =========================================

def liquidity_ok(

    exchange,

    symbol
):

    try:

        orderbook = (
            exchange.fetch_order_book(
                symbol
            )
        )

        bids = orderbook[
            'bids'
        ]

        asks = orderbook[
            'asks'
        ]

        bid_volume = sum(

            price * qty

            for price, qty in bids[:10]
        )

        ask_volume = sum(

            price * qty

            for price, qty in asks[:10]
        )

        total_volume = (
            bid_volume + ask_volume
        )

        print(
            f'ORDERBOOK VOLUME: {total_volume}'
        )

        return (
            total_volume
            >=
            MIN_ORDERBOOK_VOLUME
        )

    except Exception as e:

        print(e)

        return False