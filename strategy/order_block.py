# =========================================
# ORDER BLOCK DETECTION
# =========================================

def detect_order_block(
    df
):

    try:

        last_candle = df.iloc[-2]

        current_candle = df.iloc[-1]

        # =========================================
        # BULLISH OB
        # =========================================

        if (

            last_candle['close']
            <
            last_candle['open']

            and

            current_candle['close']
            >
            current_candle['open']
        ):

            return {

                'type': 'bullish',

                'high': last_candle['high'],

                'low': last_candle['low']
            }

        # =========================================
        # BEARISH OB
        # =========================================

        elif (

            last_candle['close']
            >
            last_candle['open']

            and

            current_candle['close']
            <
            current_candle['open']
        ):

            return {

                'type': 'bearish',

                'high': last_candle['high'],

                'low': last_candle['low']
            }

        return {

            'type': None
        }

    except Exception as e:

        print(e)

        return {

            'type': None
        }