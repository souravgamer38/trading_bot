from datetime import datetime

from analytics.logger import log_info

from config import (

    ENABLE_LONDON_SESSION,

    ENABLE_NEWYORK_SESSION,

    ENABLE_ASIAN_SESSION
)


# =========================================
# SMART SESSION FILTER
# =========================================

def smart_session():

    try:

        utc_hour = (
            datetime.utcnow().hour
        )

        # =========================================
        # ASIAN SESSION
        # =========================================

        if (

            ENABLE_ASIAN_SESSION

            and

            0 <= utc_hour <= 7
        ):

            log_info("ASIAN SESSION")

            return True

        # =========================================
        # LONDON SESSION
        # =========================================

        if (

            ENABLE_LONDON_SESSION

            and

            7 <= utc_hour <= 13
        ):

            log_info("LONDON SESSION'")

            return True

        # =========================================
        # NEW YORK SESSION
        # =========================================

        if (

            ENABLE_NEWYORK_SESSION

            and

            13 <= utc_hour <= 22
        ):

            log_info("NEW YORK SESSION")

            return True

        return False

    except Exception as e:

        print(e)

        return False