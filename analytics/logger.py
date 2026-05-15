from datetime import datetime

from config import (
    TRADE_LOG_FILE,
    ERROR_LOG_FILE,
    INFO_LOG_FILE,
    PERFORMANCE_LOG_FILE,
    DEBUG_MODE
)


# =========================================
# CURRENT TIME
# =========================================

def current_time():

    return datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S'
    )


# =========================================
# WRITE FILE
# =========================================

def write_file(
    file_path,
    message
):

    with open(
        file_path,
        'a'
    ) as file:

        file.write(
            message + '\n'
        )


# =========================================
# TRADE LOGGER
# =========================================

def log_trade(
    trade_data
):

    try:

        message = f'''

========================================
TRADE LOG
========================================

TIME:
{current_time()}

MODE:
{trade_data.get('mode')}

SYMBOL:
{trade_data.get('symbol')}

SIDE:
{trade_data.get('side')}

ENTRY:
{trade_data.get('entry')}

STOPLOSS:
{trade_data.get('sl')}

TAKEPROFIT:
{trade_data.get('tp')}

QTY:
{trade_data.get('qty')}

RR:
{trade_data.get('rr')}

RESULT:
{trade_data.get('result')}

PNL:
{trade_data.get('pnl')}

FVG SCORE:
{trade_data.get('fvg_score')}

========================================
'''

        write_file(

            TRADE_LOG_FILE,

            message
        )

        if DEBUG_MODE:

            print(
                'TRADE LOGGED'
            )

    except Exception as e:

        log_error(str(e))


# =========================================
# ERROR LOGGER
# =========================================

def log_error(
    error_message
):

    try:

        message = f'''

========================================
ERROR LOG
========================================

TIME:
{current_time()}

ERROR:
{error_message}

========================================
'''

        write_file(

            ERROR_LOG_FILE,

            message
        )

        print(
            f'ERROR: {error_message}'
        )

    except Exception as e:

        print(e)


# =========================================
# INFO LOGGER
# =========================================

def log_info(
    info
):

    try:

        message = f'''

[{current_time()}]

INFO:
{info}

'''

        write_file(
            INFO_LOG_FILE,
            message
        )

        if DEBUG_MODE:

            print(message)

    except Exception as e:

        print(e)


# =========================================
# STRATEGY LOGGER
# =========================================

def log_strategy(
    strategy_data
):

    try:

        if not DEBUG_MODE:

            return

        message = f'''

========================================
STRATEGY DEBUG
========================================

TIME:
{current_time()}

DATA:
{strategy_data}

========================================
'''

        print(
            message
        )

    except Exception as e:

        print(e)


# =========================================
# PERFORMANCE LOGGER
# =========================================

def log_performance(
    report
):

    try:

        message = f'''

========================================
PERFORMANCE REPORT
========================================

TIME:
{current_time()}

{report}

========================================
'''

        write_file(

            PERFORMANCE_LOG_FILE,

            message
        )

        if DEBUG_MODE:

            print(
                'PERFORMANCE LOGGED'
            )

    except Exception as e:

        log_error(STR (e))
