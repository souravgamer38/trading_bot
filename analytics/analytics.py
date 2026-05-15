import sqlite3
import pandas as pd

from config import (
    DATABASE_PATH
)


# =========================================
# DATABASE CONNECTION
# =========================================

def connect_db():

    return sqlite3.connect(
        DATABASE_PATH
    )


# =========================================
# LOAD TRADES
# =========================================

def load_trades():

    try:

        connection = connect_db()

        query = '''
SELECT * FROM trades
'''

        df = pd.read_sql_query(

            query,

            connection
        )

        connection.close()

        return df

    except Exception as e:

        print(e)

        return pd.DataFrame()


# =========================================
# TOTAL TRADES
# =========================================

def total_trades():

    df = load_trades()

    return len(df)


# =========================================
# TOTAL WINS
# =========================================

def total_wins():

    df = load_trades()

    if df.empty:

        return 0

    wins = df[
        df['result'] == 'TP'
    ]

    return len(wins)


# =========================================
# TOTAL LOSSES
# =========================================

def total_losses():

    df = load_trades()

    if df.empty:

        return 0

    losses = df[
        df['result'] == 'SL'
    ]

    return len(losses)


# =========================================
# WINRATE
# =========================================

def calculate_winrate():

    trades = total_trades()

    wins = total_wins()

    if trades == 0:

        return 0

    winrate = (
        wins / trades
    ) * 100

    return round(
        winrate,
        2
    )


# =========================================
# TOTAL PNL
# =========================================

def total_pnl():

    df = load_trades()

    if df.empty:

        return 0

    pnl = df[
        'pnl'
    ].sum()

    return round(
        pnl,
        2
    )


# =========================================
# AVG WIN
# =========================================

def average_win():

    df = load_trades()

    if df.empty:

        return 0

    wins = df[
        df['pnl'] > 0
    ]

    if wins.empty:

        return 0

    avg = wins[
        'pnl'
    ].mean()

    return round(
        avg,
        2
    )


# =========================================
# AVG LOSS
# =========================================

def average_loss():

    df = load_trades()

    if df.empty:

        return 0

    losses = df[
        df['pnl'] < 0
    ]

    if losses.empty:

        return 0

    avg = losses[
        'pnl'
    ].mean()

    return round(
        avg,
        2
    )


# =========================================
# PROFIT FACTOR
# =========================================

def profit_factor():

    df = load_trades()

    if df.empty:

        return 0

    gross_profit = df[
        df['pnl'] > 0
    ]['pnl'].sum()

    gross_loss = abs(

        df[
            df['pnl'] < 0
        ]['pnl'].sum()
    )

    if gross_loss == 0:

        return 0

    pf = (
        gross_profit
        /
        gross_loss
    )

    return round(
        pf,
        2
    )


# =========================================
# MAX DRAWDOWN
# =========================================

def max_drawdown():

    df = load_trades()

    if df.empty:

        return 0

    equity_curve = (
        df['pnl']
        .cumsum()
    )

    peak = equity_curve.expanding(
        min_periods=1
    ).max()

    drawdown = (
        equity_curve - peak
    )

    max_dd = drawdown.min()

    return round(
        max_dd,
        2
    )


# =========================================
# LAST TRADE
# =========================================

def last_trade():

    df = load_trades()

    if df.empty:

        return None

    return df.iloc[-1].to_dict()


# =========================================
# ANALYTICS REPORT
# =========================================

def analytics_report():

    report = f'''

=========================================
📊 BOT ANALYTICS REPORT
=========================================

Total Trades:
{total_trades()}

Wins:
{total_wins()}

Losses:
{total_losses()}

Winrate:
{calculate_winrate()}%

Total PnL:
{total_pnl()}

Average Win:
{average_win()}

Average Loss:
{average_loss()}

Profit Factor:
{profit_factor()}

Max Drawdown:
{max_drawdown()}

=========================================

'''

    print(
        report
    )

    return report
