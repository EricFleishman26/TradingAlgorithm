import pandas as pd
import attributesLib
import chooseStockLib
import buyLib
import sellLib
from classes import *

#Open file containing tickers
tickers = pd.read_csv('data.csv')
df = pd.DataFrame(tickers)

#Create Stock Objec
stocks = []
for i in range(5):
    ticker = df.loc[i, "Ticker"].strip()
    stocks.append(Stock(ticker))

#Give the Stock Objects in the stocks list all of their attributes
attributesLib.get_attributes(stocks)

#Make list of stocks to buy
buy_list = chooseStockLib.generate_buy_list(stocks)

#Buy stocks
buyLib.buy_stocks(buy_list)

#Sell stocks
sellLib.sell_stocks()

#Needs to check if stock is already owned in the Alpaca API. If the stock is already owned, the program should not buy
#If not, the program should buy
