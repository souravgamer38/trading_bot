# =========================================
# LAST SIGNAL TRACKER
# =========================================

last_signal_time = None


# =========================================
# CHECK NEW SIGNAL
# =========================================

def is_new_signal(
    signal_time
):

    global last_signal_time

    try:

        # =========================================
        # FIRST SIGNAL
        # =========================================

        if last_signal_time is None:

            last_signal_time = (
                signal_time
            )

            return True

        # =========================================
        # DUPLICATE SIGNAL
        # =========================================

        if signal_time == last_signal_time:

            return False

        # =========================================
        # NEW SIGNAL
        # =========================================

        last_signal_time = (
            signal_time
        )

        return True

    except Exception as e:

        print(e)

        return False