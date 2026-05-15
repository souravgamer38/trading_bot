from config import (
    CORRELATED_SYMBOLS
)


# =========================================
# CORRELATION FILTER
# =========================================

def correlation_ok(

    exchange,

    symbol,

    signal_type
):

    try:

        correlated_pairs = (
            CORRELATED_SYMBOLS.get(
                symbol,
                []
            )
        )

        if not correlated_pairs:

            return True

        positions = (
            exchange.fetch_positions()
        )

        # =========================================
        # CHECK OPEN POSITIONS
        # =========================================

        for position in positions:

            contracts = float(

                position.get(
                    'contracts',
                    0
                )
            )

            if contracts <= 0:

                continue

            open_symbol = (
                position.get(
                    'symbol',
                    ''
                )
            )

            position_side = (
                position.get(
                    'side',
                    ''
                ).lower()
            )

            # =========================================
            # SAME CORRELATED POSITION
            # =========================================

            if (

                open_symbol
                in
                correlated_pairs

                and

                position_side
                ==
                signal_type
            ):

                print(
                    f'CORRELATED TRADE BLOCKED: {open_symbol}'
                )

                return False

        return True

    except Exception as e:

        print(e)

        return False