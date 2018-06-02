#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from candle import Candle
from candle_patterns import CandlePatterns as P

def load_json(ticker):
    """
    load a json object for a ticker from a file with the same name
    """

    data_file_name = f"{ticker}.json"

    with open(data_file_name, 'r') as data_file:
        candles_json = data_file.read()

    return candles_json

def candle_sticks(ticker):
    """
    return daily time series candle sticks and volumes for a certain ticker
    """
    candles_json = load_json(ticker)
    time_series = json.loads(candles_json)["Time Series (Daily)"]

    candles = []
    for key in time_series.keys():
        
        candle_date = key
        candle_value = time_series[candle_date]

        volume = candle_value["5. volume"]
        open_ = candle_value["1. open"]
        close = candle_value["4. close"]
        high = candle_value["2. high"]
        low = candle_value["3. low"]
        candle_ = Candle(candle_date, volume, open_, close, high, low)
        candles.append(candle_)

    return sorted(candles)
        

if __name__ == "__main__":

    candles = candle_sticks('MELI')

    bullish_engulfing_days = [c._date for i,c in enumerate(candles) if P.bullish_engulfing(candles, i)]
    print(bullish_engulfing_days)

    #engulfing_days = [c._date for i,c in enumerate(candles) if P.engulfing(candles, i)]
    #print(engulfing_days)
