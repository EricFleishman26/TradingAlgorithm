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
for i in range(5):
    ticker = df.loc[i, "Ticker"].strip()
    stocks.append(Stock(ticker))

while True:
    market_open = tc.market_status()

    if market_open is True:
        attributesLib.get_attributes(stocks)

    while market_open is True:
        buy_list = chooseStockLib.generate_buy_list(stocks)

        buyLib.buy_stocks(buy_list)

        sellLib.sell_stocks()

        market_open = tc.market_status()



