from storage.crash_recovery import (

    save_trade,

    load_trade,

    clear_trade
)


# =========================================
# SAVE TRADE STATE
# =========================================

def save_trade_state(
    trade_data
):

    try:

        save_trade(
            trade_data
        )

        print(
            'TRADE PERSISTENCE SAVED'
        )

    except Exception as e:

        print(e)


# =========================================
# LOAD TRADE STATE
# =========================================

def load_trade_state():

    try:

        trade = load_trade()

        return trade

    except Exception as e:

        print(e)

        return None


# =========================================
# CLEAR TRADE STATE
# =========================================

def clear_trade_state():

    try:

        clear_trade()

        print(
            'TRADE PERSISTENCE CLEARED'
        )

    except Exception as e:

        print(e)