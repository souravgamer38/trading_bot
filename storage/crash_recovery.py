import json
import os

from config import (
    ACTIVE_TRADE_FILE
)


# =========================================
# SAVE TRADE
# =========================================

def save_trade(
    trade_data
):

    try:

        with open(
            ACTIVE_TRADE_FILE,
            'w'
        ) as file:

            json.dump(

                trade_data,

                file,

                indent=4
            )

        print(
            'TRADE SAVED'
        )

    except Exception as e:

        print(e)


# =========================================
# LOAD TRADE
# =========================================

def load_trade():

    try:

        if not os.path.exists(
            ACTIVE_TRADE_FILE
        ):

            return None

        with open(
            ACTIVE_TRADE_FILE,
            'r'
        ) as file:

            trade = json.load(
                file
            )

        return trade

    except Exception as e:

        print(e)

        return None


# =========================================
# CLEAR TRADE
# =========================================

def clear_trade():

    try:

        if os.path.exists(
            ACTIVE_TRADE_FILE
        ):

            os.remove(
                ACTIVE_TRADE_FILE
            )

            print(
                'TRADE CLEARED'
            )

    except Exception as e:

        print(e)