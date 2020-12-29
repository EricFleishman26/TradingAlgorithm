import alpaca_trade_api as tradeapi
import pandas as pd

key = 'PKBNCU1670FN1OZTC1K6'
sec = '5KcY3adRFfP4C40VbQTMdwYl1QBECwPqoQr9NdQa'
url = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key, sec, url, api_version='v2')

#Buys the stocks permitting they meet requirements
def buy_stocks(stocks):
    for i in stocks:
        buy = determine_if_buy(i)
        if buy is True:
            api.submit_order(symbol=str(i.ticker), qty="10", side="buy", type="market", time_in_force="day")

#Determines if a screened stock is to be bought based on 50 and 200 day moving averages
def determine_if_buy(stock):
    moving50 = stock.moving50
    moving200 = stock.moving200
    if_not_bought = check_if_bought(stock.ticker)
    if (moving50 > moving200) and if_not_bought is True:
        return True
    else:
        return False


def check_if_bought(ticker):
    positions = api.list_positions()
    df = pd.DataFrame(positions)
    bought_stocks = []

    for i in range(len(df)):
        bought_stocks.append((df.loc[i,0]).symbol)

    for i in bought_stocks:
        if i == ticker:
            return False
    return True



def get_api():
    return api
