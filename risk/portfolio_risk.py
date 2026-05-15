from config import (
    MAX_PORTFOLIO_EXPOSURE
)


# =========================================
# PORTFOLIO EXPOSURE CHECK
# =========================================

def exposure_ok(

    exchange,

    symbol,

    usd_balance,

    new_trade_value
):

    try:

        positions = (
            exchange.fetch_positions()
        )

        total_exposure = 0

        # =========================================
        # OPEN POSITIONS
        # =========================================

        for position in positions:

            contracts = float(

                position.get(
                    'contracts',
                    0
                )
            )

            entry_price = float(

                position.get(
                    'entryPrice',
                    0
                )
            )

            exposure = (
                contracts
                *
                entry_price
            )

            total_exposure += exposure

        # =========================================
        # NEW TRADE
        # =========================================

        total_exposure += (
            new_trade_value
        )

        exposure_ratio = (

            total_exposure
            /
            usd_balance
        )

        print(
            f'EXPOSURE RATIO: {exposure_ratio}'
        )

        # =========================================
        # LIMIT
        # =========================================

        if (

            exposure_ratio
            >
            MAX_PORTFOLIO_EXPOSURE
        ):

            print(
                'PORTFOLIO LIMIT EXCEEDED'
            )

            return False

        return True

    except Exception as e:

        print(e)

        return False