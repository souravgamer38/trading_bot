from storage.database import (
    load_trades
)


# =========================================
# TOTAL TRADES
# =========================================

def total_trades():

    try:

        trades = load_trades()

        return len(trades)

    except Exception as e:

        print(e)

        return 0


# =========================================
# WINNING TRADES
# =========================================

def winning_trades():

    try:

        trades = load_trades()

        wins = [

            trade

            for trade in trades

            if trade[9] == 'TP'
        ]

        return len(wins)

    except Exception as e:

        print(e)

        return 0


# =========================================
# LOSING TRADES
# =========================================

def losing_trades():

    try:

        trades = load_trades()

        losses = [

            trade

            for trade in trades

            if trade[9] == 'SL'
        ]

        return len(losses)

    except Exception as e:

        print(e)

        return 0


# =========================================
# WINRATE
# =========================================

def winrate():

    try:

        total = total_trades()

        wins = winning_trades()

        if total == 0:

            return 0

        return round(

            (wins / total) * 100,

            2
        )

    except Exception as e:

        print(e)

        return 0


# =========================================
# TOTAL PNL
# =========================================

def total_pnl():

    try:

        trades = load_trades()

        pnl = sum(

            trade[8]

            for trade in trades
        )

        return round(
            pnl,
            2
        )

    except Exception as e:

        print(e)

        return 0