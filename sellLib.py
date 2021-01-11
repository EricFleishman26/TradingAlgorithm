import buyLib
import pandas as pd
from classes import *

def sell_stocks(stocks):
    api = buyLib.get_api()
    positions = api.list_positions()
    my_tickers = get_owned_tickers(positions)

    for i in my_tickers:
        for j in stocks:
            if j.ticker == i:
                i = Stock(i)
                match_attributes(i, j)
                if i.moving50 < i.moving200:
                    api.submit_order(symbol=i.ticker, qty="10", side="sell", type="market", time_in_force="day")

def get_owned_tickers(positions):
    df = pd.DataFrame(positions)
    tickers = []
    for i in range(len(df)):
        tickers.append(df.loc[i,0].symbol)

    return tickers


def match_attributes(stock_i, stock_j):
    stock_i.moving50 = stock_j.moving50
    stock_i.moving200 = stock_j.moving200

