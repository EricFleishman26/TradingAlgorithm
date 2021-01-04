import buyLib
import pandas as pd
from classes import *

def sell_stocks(stocks):
    api = buyLib.get_api()
    positions = api.list_positions()
    my_tickers = get_owned_tickers(positions)

    for i in my_tickers:
        i = Stock(i)
        for j in stocks:
            if j.ticker == i.ticker:
                i = j
                testy = i.moving50
                testy2 = i.moving200
                if i.moving50 < i.moving200:
                    test = i.ticker
                    api.submit_order(symbol=i.ticker, qty="10", side="sell", type="market", time_in_force="day")

def get_owned_tickers(positions):
    df = pd.DataFrame(positions)
    tickers = []
    for i in range(len(df)):
        tickers.append(df.loc[i,0].symbol)

    return tickers
