import pandas as pd
import attributesLib
import chooseStockLib
import buyLib
import sellLib
import timeControl as tc
from classes import *

tickers = pd.read_csv('data.csv')
df = pd.DataFrame(tickers)

stocks = []
stored_stocks = []
for i in range(len(df)):
    ticker = df.loc[i, "Ticker"].strip()
    stocks.append(Stock(ticker))

while True:
    market_open = tc.market_status()

    if market_open is True and len(stored_stocks) < 1:
        attributesLib.get_attributes(stocks)
        stored_stocks = stocks

    while market_open is True:
        buy_list = chooseStockLib.generate_buy_list(stocks)

        buyLib.buy_stocks(buy_list)

        try:
            sellLib.sell_stocks(stored_stocks)
        except:
            print("Nothing to sell, no Stocks Owned...")

        attributesLib.refresh_moving(stocks)

        market_open = tc.market_status()



