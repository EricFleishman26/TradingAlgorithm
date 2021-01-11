import pandas as pd
import attributesLib
import chooseStockLib
import buyLib
import sellLib
import timeControl as tc
from classes import *

stock_data = pd.read_csv('scraped_stocks.txt', sep=" ")
df = pd.DataFrame(stock_data)
stocks = []

for i in range(55):
    stocks.append(Stock(df.loc[i, "Ticker"].strip()))

while True:
    stock_data = pd.read_csv('scraped_stocks.txt', sep=" ")
    df = pd.DataFrame(stock_data)
    attributesLib.get_attributes(stocks, df)

    market_open = tc.market_status()

    while market_open is True:
        buy_list = chooseStockLib.generate_buy_list(stocks)

        buyLib.buy_stocks(buy_list)

        try:
            sellLib.sell_stocks(stocks)
        except:
            print("Nothing to sell, no Stocks Owned...")

        market_open = tc.market_status()
