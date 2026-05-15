# =========================================
# FAIR VALUE GAP DETECTION
# =========================================

def detect_fvg(
    df
):

    signals = []

    try:

        for i in range(2, len(df)):

            first = df.iloc[i - 2]

            second = df.iloc[i - 1]

            third = df.iloc[i]

            # =========================================
            # BULLISH FVG
            # =========================================

            if (

                first['high']
                <
                third['low']
            ):

                signals.append({

                    'time': third['time'],

                    'type': 'bullish',

                    'gap_high': third['low'],

                    'gap_low': first['high'],

                    'high': third['high'],

                    'low': third['low']
                })

            # =========================================
            # BEARISH FVG
            # =========================================

            elif (

                first['low']
                >
                third['high']
            ):

                signals.append({

                    'time': third['time'],

                    'type': 'bearish',

                    'gap_high': first['low'],

                    'gap_low': third['high'],

                    'high': third['high'],

                    'low': third['low']
                })

        return signals

    except Exception as e:

        print(e)

        return []