import sqlite3

from config import (
    DATABASE_PATH
)


# =========================================
# CONNECT DATABASE
# =========================================

def connect_db():

    return sqlite3.connect(
        DATABASE_PATH
    )


# =========================================
# INITIALIZE DATABASE
# =========================================

def initialize_database():

    try:

        connection = connect_db()

        cursor = connection.cursor()

        cursor.execute(
'''
CREATE TABLE IF NOT EXISTS trades (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symbol TEXT,

    side TEXT,

    entry REAL,

    sl REAL,

    tp REAL,

    qty REAL,

    rr REAL,

    pnl REAL,

    result TEXT,

    fvg_score REAL,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
'''
        )

        connection.commit()

        connection.close()

        print(
            'DATABASE INITIALIZED'
        )

    except Exception as e:

        print(e)


# =========================================
# SAVE TRADE
# =========================================

def save_trade_db(

    symbol,

    side,

    entry,

    sl,

    tp,

    qty,

    rr,

    pnl,

    result,

    fvg_score
):

    try:

        connection = connect_db()

        cursor = connection.cursor()

        cursor.execute(
'''
INSERT INTO trades (

    symbol,
    side,
    entry,
    sl,
    tp,
    qty,
    rr,
    pnl,
    result,
    fvg_score

)

VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''',

            (

                symbol,

                side,

                entry,

                sl,

                tp,

                qty,

                rr,

                pnl,

                result,

                fvg_score
            )
        )

        connection.commit()

        connection.close()

        print(
            'TRADE SAVED TO DATABASE'
        )

    except Exception as e:

        print(e)


# =========================================
# LOAD TRADES
# =========================================

def load_trades():

    try:

        connection = connect_db()

        cursor = connection.cursor()

        cursor.execute(
'''
SELECT * FROM trades
'''
        )

        rows = cursor.fetchall()

        connection.close()

        return rows

    except Exception as e:

        print(e)

        return []