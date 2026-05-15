import os

from dotenv import load_dotenv

load_dotenv()

# =========================================
# BOT MODE
# =========================================

# CHANGE THIS ONLY 👇

# PAPER
# LIVE

TRADING_MODE = 'PAPER'


# =========================================
# PAPER TRADING SETTINGS
# =========================================

PAPER_BALANCE = 1000


# =========================
# DELTA API
# =========================

API_KEY = os.getenv(
    'API_KEY'
)

API_SECRET = os.getenv(
    'API_SECRET'
)


# =========================
# TELEGRAM
# =========================

TELEGRAM_BOT_TOKEN = os.getenv(
    'TELEGRAM_BOT_TOKEN'
)

TELEGRAM_CHAT_ID = os.getenv(
    'TELEGRAM_CHAT_ID'
)


# =========================================
# NEWS API
# =========================================

NEWS_API_KEY = os.getenv(
    'NEWS_API_KEY'
)
HIGH_IMPACT_HOURS = [
    "18:00",
    "18:30",
    "20:00",
    "23:30",
    "00:30"
]


# =========================================
# TRADING SETTINGS
# =========================================

SYMBOL = 'ETHUSDT'

TIMEFRAME = '15m'

HTF_TIMEFRAME = '1h'


# =========================================
# INDICATORS
# =========================================

EMA_PERIOD = 200

ATR_PERIOD = 14


# =========================================
# RISK SETTINGS
# =========================================

RISK_PERCENT = 5

MAX_DAILY_LOSS_PERCENT = 5

MAX_LOT_SIZE = 10


# =========================================
# TRADE FREQUENCY
# =========================================

MAX_TRADES_PER_DAY = 5

MAX_TRADES_PER_SESSION = 2


# =========================================
# PORTFOLIO EXPOSURE
# =========================================

MAX_PORTFOLIO_EXPOSURE = 0.30


# =========================================
# DYNAMIC STOPLOSS
# =========================================

ATR_SL_MULTIPLIER = 1.5


# =========================================
# ATR TRAILING
# =========================================

ATR_TRAILING_MULTIPLIER = 1.0


# =========================================
# DYNAMIC RR
# =========================================

MIN_RR = 1.5

MAX_RR = 5


# =========================================
# FVG QUALITY SCORE
# =========================================

MIN_FVG_SCORE = 5


# =========================================
# DISPLACEMENT FILTER
# =========================================

MIN_DISPLACEMENT_RATIO = 0.60


# =========================================
# IMBALANCE FILTER
# =========================================

MIN_IMBALANCE_ATR_RATIO = 0.30


# =========================================
# SPREAD FILTER
# =========================================

MAX_SPREAD_PERCENT = 0.10


# =========================================
# LIQUIDITY FILTER
# =========================================

MIN_ORDERBOOK_VOLUME = 100000


# =========================================
# VOLUME FILTER
# =========================================

MIN_VOLUME_RATIO = 1.5


# =========================================
# VOLATILITY POSITION SIZING
# =========================================

HIGH_VOLATILITY_THRESHOLD = 0.02

MEDIUM_VOLATILITY_THRESHOLD = 0.01


# =========================================
# CORRELATION FILTER
# =========================================

CORRELATED_SYMBOLS = {

    'ETHUSDT': [
        'BTCUSDT'
    ],

    'BTCUSDT': [
        'ETHUSDT'
    ]
}


# =========================================
# COOLDOWN
# =========================================

COOLDOWN_SECONDS = 900


# =========================================
# RATE LIMIT
# =========================================

MIN_REQUEST_INTERVAL = 0.25


# =========================================
# DATABASE
# =========================================

DATABASE_PATH = (
    'data/trading_bot.db'
)


# =========================================
# JSON STATE FILES
# =========================================

BOT_STATE_FILE = (
    'data/bot_state.json'
)

ACTIVE_TRADE_FILE = (
    'data/active_trade_state.json'
)

PERFORMANCE_FILE = (
    'data/performance.json'
)

PERIODIC_REPORT_FILE = (
    'data/periodic_reports.json'
)


# =========================================
# LOG FILES
# =========================================


TRADE_LOG_FILE = 'logs/trades.log'

ERROR_LOG_FILE = 'logs/errors.log'

INFO_LOG_FILE = 'logs/info.log'

PERFORMANCE_LOG_FILE = 'logs/performance.log'


# =========================================
# SESSION FILTER
# =========================================

ENABLE_LONDON_SESSION = True

ENABLE_NEWYORK_SESSION = True

ENABLE_ASIAN_SESSION = False


# =========================================
# SMART MONEY FILTERS
# =========================================

ENABLE_FVG = True

ENABLE_BOS = True

ENABLE_CHOCH = True

ENABLE_ORDER_BLOCK = True

ENABLE_LIQUIDITY_SWEEP = True


# =========================================
# FEATURES
# =========================================

ENABLE_TELEGRAM = True

ENABLE_DATABASE = True

ENABLE_PERFORMANCE_REPORTS = True

ENABLE_AUTO_RESTART = True

ENABLE_CRASH_RECOVERY = True

ENABLE_RATE_LIMIT_HANDLER = True

ENABLE_DYNAMIC_RR = True

ENABLE_DYNAMIC_SL = True

ENABLE_TRAILING_STOP = True

ENABLE_VOLUME_FILTER = True

ENABLE_NEWS_FILTER = True

USE_NEWS_API = True


# =========================================
# DEBUG
# =========================================

DEBUG_MODE = False


# =========================================
# CONFIG VALIDATION
# =========================================

VALID_MODES = [

    'PAPER',

    'LIVE'
]
