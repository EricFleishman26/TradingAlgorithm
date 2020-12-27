import buyLib
import attributesLib
from classes import *

#Sells stocks that are determined to be sold
def sell_stocks():
    api = buyLib.connect_api()
    current_positions = api.list_positions()
    stocks = get_stock_objects(current_positions)
    attributesLib.get_attributes(stocks)

    for i in stocks:
        sell = determine_if_sell(i)
        if sell is True:
            api.submit_order(symbol=str(i.ticker), qty="10", side="sell", type="market", time_in_force="day")

#Takes the tickers returned by the Alpaca API and makes them into Stock Objects
def get_stock_objects(list):
    objects = []
    for i in list:
        objects.append(Stock(i.symbol))
    return objects

#Determines if a stock is to be sold based on 50 and 200 day moving averages
def determine_if_sell(stock):
    moving50 = stock.moving50
    moving200 = stock.moving200
    if moving50 < moving200:
        return True
    else:
        return False
