#!/usr/bin/env python
# -*- coding: utf-8 -*-

from candle import Candle

class CandlePatterns:
    """
    common candle stick patterns as in https://www.stocktrader.com/2013/03/02/candlestick-patterns-stocks-traders-investing/
    """

    @staticmethod
    def bullish_day(candles, index):
        """
        if this day closes lower than open
        """
        return candles[index].bullish()
    
    @staticmethod
    def bearish_day(candles, index):
        """
        if this day closes lower than open
        """
        return candles[index].bearish()

    @staticmethod
    def engulfing(candles, index):
        """
        given a candles series and index to one of its data,
        return if this day has a higher high and lower low than yesterday
        """
        if not index:
            return False

        candle_today = candles[index]
        candle_yesterday = candles[index - 1]

        return candle_today._high > candle_yesterday._high \
                and candle_today._low < candle_yesterday._low \

    @staticmethod
    def bullish_engulfing(candles, index):
        """
        given a candles series and an index to one of its data,
        return if this trading day has a bullish engulfing pattern.
        """
        return CandlePatterns.bullish_day(candles, index) and CandlePatterns.engulfing(candles, index)

    @staticmethod
    def bearish_engulfing(candles, index):
        """
        given a candles series and an index to one of its data,
        return if this trading day has a bearish engulfing pattern.
        """
        return CandlePatterns.bearish_day(candles, index) and CandlePatterns.engulfing(candles, index)

    @staticmethod
    def hammer_reversal(candles, index):
        """
        given a candles series and an index to one of its data,
        return if this trading day has a hammer_reversal pattern
        """
        return CandlePatterns.hammer_reversal_head(candles, index) \
                or CandlePatterns.hammer_reversal_foot(candles, index)

    @staticmethod
    def hammer_reversal_head(candles, index):
        candle_today = candles[index]
        diff_oc = abs(candle_today.diff_open_close())
        diff_hl = abs(candle_today.diff_high_low())

        mid_oc = candle_today.mid_open_close()

        return diff_hl*0.1 < diff_oc < diff_hl*0.2 \
                and candle_today._high - mid_oc < 0.3*diff_hl

    @staticmethod
    def hammer_reversal_foot(candles, index):
        candle_today = candles[index]
        diff_oc = abs(candle_today.diff_open_close())
        diff_hl = abs(candle_today.diff_high_low())

        mid_oc = candle_today.mid_open_close()

        return diff_hl*0.1 < diff_oc < diff_hl*0.2 \
                and mid_oc - candle_today._low < 0.3*diff_hl
