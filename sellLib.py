import buyLib
import attributesLib
import pandas as pd
from classes import *

#Sells stocks that are determined to be sold
def sell_stocks():
    api = buyLib.get_api()
    positions = api.list_positions()
    df = pd.DataFrame(positions)
    stocks = get_stock_objects(df)
    attributesLib.get_attributes(stocks)

    for i in stocks:
        sell = determine_if_sell(i)
        if sell is True:
            print("Selling: ", i.ticker)
            api.submit_order(symbol=str(i.ticker), qty="10", side="sell", type="market", time_in_force="day")
        else:
            print("Not Selling: ", i.ticker)

#Takes the tickers returned by the Alpaca API and makes them into Stock Objects
def get_stock_objects(df):
    objects = []
    for i in range(len(df)):
        ticker = df.loc[i,0]
        objects.append(Stock(ticker.symbol))
    return objects

#Determines if a stock is to be sold based on 50 and 200 day moving averages
def determine_if_sell(stock):
    moving50 = stock.moving50
    moving200 = stock.moving200
    if moving50 < moving200:
        return True
    else:
        return False

#PLAN FOR REVISION: Needs to take the stocks already owned from the API and get their attributes from the attribute list already stored. Doing this would speed up program's
#Execution time