from datetime import datetime

from analytics.analytics import (
    load_trades
)

from telegram.telegram_bot import (
    send_telegram
)


# =========================================
# FILTER BY DATE
# =========================================

def filter_period(
    df,
    period
):

    now = datetime.now()

    df['timestamp'] = (
        df['timestamp']
        .astype(str)
    )

    df['timestamp'] = (
        df['timestamp']
        .apply(
            lambda x:
            datetime.fromisoformat(x)
        )
    )

    if period == 'daily':

        filtered = df[

            df['timestamp'].dt.date
            ==
            now.date()
        ]

    elif period == 'weekly':

        filtered = df[

            df['timestamp']
            >=
            now.replace(day=1)
        ]

    elif period == 'monthly':

        filtered = df[

            df['timestamp'].dt.month
            ==
            now.month
        ]

    else:

        filtered = df

    return filtered


# =========================================
# CREATE REPORT
# =========================================

def create_report(
    period
):

    try:

        df = load_trades()

        if df.empty:

            return None

        df = filter_period(
            df,
            period
        )

        if df.empty:

            return None

        total = len(df)

        wins = len(

            df[
                df['result'] == 'TP'
            ]
        )

        losses = len(

            df[
                df['result'] == 'SL'
            ]
        )

        pnl = round(

            df['pnl'].sum(),

            2
        )

        if total > 0:

            winrate = round(

                (wins / total) * 100,

                2
            )

        else:

            winrate = 0

        report = f'''

=========================================
📊 {period.upper()} REPORT
=========================================

Trades:
{total}

Wins:
{wins}

Losses:
{losses}

Winrate:
{winrate}%

PnL:
{pnl}

=========================================
'''

        return report

    except Exception as e:

        print(e)

        return None


# =========================================
# DAILY REPORT
# =========================================

def daily_report():

    report = create_report(
        'daily'
    )

    if report:

        print(report)

        send_telegram(
            report
        )


# =========================================
# WEEKLY REPORT
# =========================================

def weekly_report():

    report = create_report(
        'weekly'
    )

    if report:

        print(report)

        send_telegram(
            report
        )


# =========================================
# MONTHLY REPORT
# =========================================

def monthly_report():

    report = create_report(
        'monthly'
    )

    if report:

        print(report)

        send_telegram(
            report
        )


# =========================================
# SEND PERIODIC REPORTS
# =========================================

def send_periodic_reports():

    now = datetime.now()

    # =========================================
    # DAILY
    # =========================================

    if (

        now.hour == 23

        and

        now.minute >= 55
    ):

        daily_report()

    # =========================================
    # WEEKLY
    # =========================================

    if (

        now.weekday() == 6

        and

        now.hour == 23

        and

        now.minute >= 55
    ):

        weekly_report()

    # =========================================
    # MONTHLY
    # =========================================

    if (

        now.day == 1

        and

        now.hour == 0

        and

        now.minute <= 5
    ):

        monthly_report()
