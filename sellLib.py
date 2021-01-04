import buyLib
import attributesLib
import pandas as pd
from classes import *

#Sells stocks that are determined to be sold
def sell_stocks(stored):
    owned_tickers = get_api_tickers()
    api = buyLib.get_api()

    for i in owned_tickers:
        for j in stored:
            if i == j.ticker:
                i = j
    for i in owned_tickers:
        if i.moving50 < i.moving200:
            api.submit_order(symbol=str(i.ticker), qty="10", side="sell", type="market", time_in_force="day")


def get_api_tickers():
    tickers = []
    api = buyLib.get_api()
    positions = api.list_positions()
    df = pd.DataFrame(positions)

    for i in range(len(df)):
        tickers.append(Stock(df.loc[i,0].symbol))

    return tickers
