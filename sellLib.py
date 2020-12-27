import buyLib
import attributesLib
from classes import *

def sell_stocks():
    api = buyLib.connect_api()
    current_positions = api.list_positions()
    stocks = get_stock_objects(current_positions)
    attributesLib.get_attributes(stocks)

    for i in stocks:
        sell = determine_if_sell(i)
        if sell is True:
            api.submit_order(symbol=str(i.ticker), qty="10", side="sell", type="market", time_in_force="day")

def get_stock_objects(list):
    objects = []
    for i in list:
        objects.append(Stock(i))
    return objects

def determine_if_sell(stock):
    moving50 = stock.moving50
    moving200 = stock.moving200
    if moving50 < moving200:
        return True
    else:
        return False
