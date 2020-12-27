import alpaca_trade_api as tradeapi

#Buys the stocks permitting they meet requirements
def buy_stocks(stocks):
    api = connect_api()

    for i in stocks:
        buy = determine_if_buy(i)
        if buy is True:
            api.submit_order(symbol=str(i.ticker), qty="10", side="buy", type="market", time_in_force="day")

#Determines if a screened stock is to be bought based on 50 and 200 day moving averages
def determine_if_buy(stock):
    moving50 = stock.moving50
    moving200 = stock.moving200
    if moving50 > moving200:
        return True
    else:
        return False

#Connects to the Alpaca API
def connect_api():
    key = 'PKE4BWTD60R2QN1WMSM1'
    sec = 'gVsggan9QBKw3AcyZuCdDZM9f3oz4r5U1LanYS3x'
    url = 'https://paper-api.alpaca.markets'
    api = tradeapi.REST(key, sec, url, api_version='v2')
    return api