import json
import os

from config import (
    PERFORMANCE_FILE
)

from analytics.analytics import (

    total_trades,

    total_wins,

    total_losses,

    calculate_winrate,

    total_pnl,

    profit_factor,

    max_drawdown
)


# =========================================
# INITIALIZE PERFORMANCE FILE
# =========================================

def initialize_performance():

    try:

        if not os.path.exists(
            PERFORMANCE_FILE
        ):

            data = {

                'total_trades': 0,

                'wins': 0,

                'losses': 0,

                'winrate': 0,

                'total_pnl': 0,

                'profit_factor': 0,

                'max_drawdown': 0
            }

            with open(
                PERFORMANCE_FILE,
                'w'
            ) as file:

                json.dump(

                    data,

                    file,

                    indent=4
                )

    except Exception as e:

        print(e)


# =========================================
# GENERATE REPORT
# =========================================

def generate_report():

    try:

        initialize_performance()

        report = {

            'total_trades': total_trades(),

            'wins': total_wins(),

            'losses': total_losses(),

            'winrate': calculate_winrate(),

            'total_pnl': total_pnl(),

            'profit_factor': profit_factor(),

            'max_drawdown': max_drawdown()
        }

        with open(
            PERFORMANCE_FILE,
            'w'
        ) as file:

            json.dump(

                report,

                file,

                indent=4
            )

        text = f'''

=========================================
📊 PERFORMANCE REPORT
=========================================

Total Trades:
{report['total_trades']}

Wins:
{report['wins']}

Losses:
{report['losses']}

Winrate:
{report['winrate']}%

Total PnL:
{report['total_pnl']}

Profit Factor:
{report['profit_factor']}

Max Drawdown:
{report['max_drawdown']}

=========================================
'''

        return text

    except Exception as e:

        print(e)

        return 'REPORT ERROR'
