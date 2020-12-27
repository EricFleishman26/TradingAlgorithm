import attributesLib

url_summ ='https://finance.yahoo.com/quote/{}?p={}'
url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'

#Generates the screened buy list
def generate_buy_list(stocks):
    list = []
    for i in stocks:
        fair_price = i.fair_val
        current_price = get_current_price(i)
        check = check_irreg(fair_price, current_price)
        if check is True:
            irreg_stock(i, list)
        else:
            if current_price <= fair_price*1.25:
                list.append(i)
    return list

#Checks if a stock is irregular
def check_irreg(fair, current):
    ratio = fair / current
    if ratio >= 5:
        return True
    else:
        return False

#Handles irregular stocks based on their Profit Margins
def irreg_stock(stock, list):
    ticker = stock.ticker
    json_data = attributesLib.get_json(url_stats, ticker)
    profit_margin = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']['profitMargins']['raw']
    if profit_margin >= 0.15:
        list.append(stock)

#Gets the current price of each stock
def get_current_price(stock):
    ticker = stock.ticker
    json_data = attributesLib.get_json(url_summ, ticker)
    price = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['regularMarketPrice']['raw']
    return price
