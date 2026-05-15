from datetime import datetime

from config import (

    ENABLE_NEWS_FILTER,

    USE_NEWS_API,

    HIGH_IMPACT_HOURS,

    NEWS_API_KEY
)


# =========================================
# OPTIONAL API IMPORT
# =========================================

if USE_NEWS_API:

    import requests


# =========================================
# HIGH IMPACT EVENTS
# =========================================

HIGH_IMPACT_EVENTS = [

    'FOMC',

    'CPI',

    'NFP',

    'Interest Rate',

    'Fed'
]


# =========================================
# FIXED VOLATILITY HOURS
# =========================================

def fixed_news_block():

    try:

        current_hour = (
            datetime.utcnow().hour
        )

        # =========================================
        # HIGH VOLATILITY HOURS
        # =========================================

        if current_hour in HIGH_IMPACT_HOURS:

            print(
                'HIGH IMPACT TIME BLOCKED'
            )

            return False

        return True

    except Exception as e:

        print(e)

        return True


# =========================================
# API NEWS FILTER
# =========================================

def api_news_filter():

    try:

        today = (
            datetime.utcnow()
            .strftime('%Y-%m-%d')
        )

        url = f'''

https://financialmodelingprep.com/api/v3/economic_calendar

?from={today}

&to={today}

&apikey={NEWS_API_KEY}

'''

        response = requests.get(
            url.strip()
        )

        events = response.json()

        current_hour = (
            datetime.utcnow().hour
        )

        # =========================================
        # CHECK EVENTS
        # =========================================

        for event in events:

            event_name = (
                event.get(
                    'event',
                    ''
                )
            )

            event_time = (
                event.get(
                    'date',
                    ''
                )
            )

            for keyword in HIGH_IMPACT_EVENTS:

                if keyword.lower() in event_name.lower():

                    try:

                        event_hour = int(

                            event_time
                            .split(' ')[1]
                            .split(':')[0]
                        )

                    except:

                        continue

                    # =========================================
                    # BLOCK WINDOW
                    # =========================================

                    if abs(

                        current_hour
                        -
                        event_hour

                    ) <= 1:

                        print(
                            f'NEWS BLOCKED: {event_name}'
                        )

                        return False

        return True

    except Exception as e:

        print(e)

        return True


# =========================================
# MAIN NEWS FILTER
# =========================================

def news_safe():

    try:

        # =========================================
        # FEATURE DISABLED
        # =========================================

        if not ENABLE_NEWS_FILTER:

            return True

        # =========================================
        # FIXED TIME FILTER
        # =========================================

        fixed_safe = (
            fixed_news_block()
        )

        if not fixed_safe:

            return False

        # =========================================
        # API FILTER
        # =========================================

        if USE_NEWS_API:

            api_safe = (
                api_news_filter()
            )

            if not api_safe:

                return False

        return True

    except Exception as e:

        print(e)

        return True