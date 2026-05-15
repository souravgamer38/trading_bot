import json
import os

from config import (
    BOT_STATE_FILE
)


# =========================================
# DEFAULT STATE
# =========================================

DEFAULT_STATE = {

    'bot_running': True,

    'last_trade_time': 0,

    'active_trade': None
}


# =========================================
# SAVE STATE
# =========================================

def save_state(
    state
):

    try:

        with open(
            BOT_STATE_FILE,
            'w'
        ) as file:

            json.dump(

                state,

                file,

                indent=4
            )

    except Exception as e:

        print(e)


# =========================================
# LOAD STATE
# =========================================

def load_state():

    try:

        if not os.path.exists(
            BOT_STATE_FILE
        ):

            save_state(
                DEFAULT_STATE
            )

            return DEFAULT_STATE

        with open(
            BOT_STATE_FILE,
            'r'
        ) as file:

            state = json.load(
                file
            )

        return state

    except Exception as e:

        print(e)

        return DEFAULT_STATE


# =========================================
# UPDATE STATE
# =========================================

def update_state(

    key,

    value
):

    try:

        state = load_state()

        state[key] = value

        save_state(
            state
        )

    except Exception as e:

        print(e)


# =========================================
# SAVE ACTIVE TRADE
# =========================================

def save_active_trade(
    trade_data
):

    try:

        state = load_state()

        state[
            'active_trade'
        ] = trade_data

        save_state(
            state
        )

        print(
            'ACTIVE TRADE SAVED'
        )

    except Exception as e:

        print(e)


# =========================================
# LOAD ACTIVE TRADE
# =========================================

def load_active_trade():

    try:

        state = load_state()

        return state.get(
            'active_trade'
        )

    except Exception as e:

        print(e)

        return None


# =========================================
# CLEAR ACTIVE TRADE
# =========================================

def clear_active_trade():

    try:

        state = load_state()

        state[
            'active_trade'
        ] = None

        save_state(
            state
        )

        print(
            'ACTIVE TRADE CLEARED'
        )

    except Exception as e:

        print(e)