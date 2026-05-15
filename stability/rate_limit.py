import time

from config import (
    MIN_REQUEST_INTERVAL
)


# =========================================
# RATE LIMIT HANDLER
# =========================================

class RateLimiter:

    def __init__(self):

        self.last_request = 0

    # =========================================
    # SAFE REQUEST
    # =========================================

    def safe_request(

        self,

        api_function,

        *args,

        **kwargs
    ):

        try:

            current_time = (
                time.time()
            )

            elapsed = (

                current_time
                -
                self.last_request
            )

            # =========================================
            # WAIT
            # =========================================

            if (

                elapsed
                <
                MIN_REQUEST_INTERVAL
            ):

                wait_time = (

                    MIN_REQUEST_INTERVAL
                    -
                    elapsed
                )

                time.sleep(
                    wait_time
                )

            result = api_function(

                *args,

                **kwargs
            )

            self.last_request = (
                time.time()
            )

            return result

        except Exception as e:

            print(e)

            return None


# =========================================
# GLOBAL INSTANCE
# =========================================

rate_limiter = RateLimiter()