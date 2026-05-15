# =========================================
# ACTIVE TRADE REGISTRY
# =========================================

active_trade = {

    'active': False,

    'symbol': None,

    'side': None,

    'entry': None,

    'sl': None,

    'tp': None,

    'qty': None
}


# =========================================
# SET ACTIVE TRADE
# =========================================

def set_active_trade(
    trade_data
):

    global active_trade

    active_trade = {

        'active': True,

        'symbol': trade_data.get(
            'symbol'
        ),

        'side': trade_data.get(
            'side'
        ),

        'entry': trade_data.get(
            'entry'
        ),

        'sl': trade_data.get(
            'sl'
        ),

        'tp': trade_data.get(
            'tp'
        ),

        'qty': trade_data.get(
            'qty'
        )
    }

    print(
        'ACTIVE TRADE REGISTERED'
    )


# =========================================
# CLEAR ACTIVE TRADE
# =========================================

def clear_active_trade():

    global active_trade

    active_trade = {

        'active': False,

        'symbol': None,

        'side': None,

        'entry': None,

        'sl': None,

        'tp': None,

        'qty': None
    }

    print(
        'ACTIVE TRADE CLEARED'
    )


# =========================================
# CHECK ACTIVE TRADE
# =========================================

def has_active_trade():

    return active_trade[
        'active'
    ]


# =========================================
# GET ACTIVE TRADE
# =========================================

def get_active_trade():

    return active_trade