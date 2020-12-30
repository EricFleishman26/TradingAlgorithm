import pandas as pd
import attributesLib
import chooseStockLib
import buyLib
import sellLib
import timeControl as tc
from classes import *

#Open file containing tickers
tickers = pd.read_csv('data.csv')
df = pd.DataFrame(tickers)

#Create Stock Object
stocks = []
for i in range(55):
    ticker = df.loc[i, "Ticker"].strip()
    stocks.append(Stock(ticker))

market_open = tc.market_status()

#If market is open get all of the attributes for the stocks
if market_open is True:
    attributesLib.get_attributes(stocks)

while market_open is True:
    #Make list of stocks to buy
    buy_list = chooseStockLib.generate_buy_list(stocks)

    #Buy stocks
    buyLib.buy_stocks(buy_list)

    #Sell stocks
    sellLib.sell_stocks(stocks)

    market_open = tc.market_status()
