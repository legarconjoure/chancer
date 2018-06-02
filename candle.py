#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Candle:

    def __init__(self, date, volume, open_, close, high, low):
        self._date = date
        self._volume = volume
        self._open = open_
        self._close = close
        self._high = high
        self._low = low

    def __eq__(self, other):
        return NotImplemented

    def __lt__(self, other):
        return self._date < other._date

    def __gt__(self, other):
        return self._date > other._date

    def bearish(self):
        return self._close < self._open

    def bullish(self):
        return self._close >= self._open

    def diff_open_close(self):
        return self._close - self._open

    def diff_high_low(self):
        return self._high - self._low

    def mid_open_close(self):
        return (self._open + self._close) / 2

    def __repr__(self):
        return f"""\
                Date {self._date}
    Volume: {self._volume}
    Open: {self._open}
    Close: {self._close}
    High: {self._high}
    Low: {self._low}
    """
