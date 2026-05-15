from config import (

    TRADING_MODE,

    VALID_MODES,

    API_KEY,

    API_SECRET,

    SYMBOL,

    TIMEFRAME,

    RISK_PERCENT
)


# =========================================
# VALIDATE CONFIG
# =========================================

def validate_config():

    try:

        # =========================================
        # TRADING MODE
        # =========================================

        if TRADING_MODE not in VALID_MODES:

            print(
                'INVALID TRADING MODE'
            )

            return False

        # =========================================
        # API KEYS
        # =========================================

        if TRADING_MODE == 'LIVE':

            if (

                API_KEY == ''

                or

                API_SECRET == ''
            ):

                print(
                    'LIVE API KEYS MISSING'
                )

                return False

        # =========================================
        # SYMBOL
        # =========================================

        if SYMBOL == '':

            print(
                'SYMBOL MISSING'
            )

            return False

        # =========================================
        # TIMEFRAME
        # =========================================

        if TIMEFRAME == '':

            print(
                'TIMEFRAME MISSING'
            )

            return False

        # =========================================
        # RISK
        # =========================================

        if (

            RISK_PERCENT <= 0

            or

            RISK_PERCENT > 10
        ):

            print(
                'INVALID RISK'
            )

            return False

        print(
            'CONFIG VALIDATED'
        )

        return True

    except Exception as e:

        print(e)

        return False