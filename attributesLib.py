import pandas as pd
import re
import json
from bs4 import BeautifulSoup
import requests

#Necessary Yahoo Finance URLs
url_summ = 'https://finance.yahoo.com/quote/{}?p={}'
url_analysis = 'https://finance.yahoo.com/quote/{}/analysis?p={}'
url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

#Assigns all Stock Objects their attributes
def get_attributes(stocks):
    for i in stocks:
        print(i.ticker)
        i.eps = get_eps(i)
        i.growth= get_growth(i)
        i.pe_ratio = get_pe_ratio(i)
        i.fair_val = get_current_fair_value(i)
        i.moving50 = get_moving(i, 50)
        i.moving200 = get_moving(i, 200)

#Gets the EPS(TTM) of the stocks
def get_eps(stock):
    json_data = get_json(url_summ, stock.ticker)
    eps = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']['trailingEps']['raw']
    return eps

#Gets the growth rates (+5y per annum) of the stocks
def get_growth(stock):
    json_data = get_json(url_analysis, stock.ticker)
    growth_data = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['earningsTrend']['trend']
    df = pd.DataFrame(growth_data)
    growth = df.loc[4, 'growth']
    return growth['raw']

#Gets the trailing (or forward) PE Ratios of the stocks
def get_pe_ratio(stock):
    json_data = get_json(url_stats, stock.ticker)
    try:
        pe = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['trailingPE']['raw']
    except:
        pe = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['forwardPE']['raw']
    return pe

#Gets the current fair value of each stock
def get_current_fair_value(stock):
    projected_values = get_projected_fair_values(stock)
    return projected_values[0]

#Makes the 5 year projections of fair values for each stock
def get_projected_fair_values(stock):
    values = []
    projected = []
    earnings = get_earnings(stock)
    pe_ratio = stock.pe_ratio
    divisor = 1 + stock.min_return
    ins_val = earnings[4] * pe_ratio

    for i in range(5):
        if i == 0:
            values.append(ins_val)
        else:
            ins_val = ins_val / divisor
            values.append(ins_val)
    for i in values[::-1]:
        projected.append(i)
    return projected

#Calculates the 5 year projected earnings of each stock
def get_earnings(stock):
    eps = stock.eps
    growth = stock.growth
    earnings = []
    for i in range(5):
        earnings.append(eps)
        eps = eps + (eps * growth)
    return earnings

#Gets the 50 and 200 day moving averages
def get_moving(stock, days):
    json_data = get_json(url_summ, stock.ticker)
    if days == 50:
        moving = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['fiftyDayAverage']['raw']
    elif days == 200:
        moving = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['twoHundredDayAverage']['raw']
    return moving

#Gets json data from URL
def get_json(url, ticker):
    response = requests.get(url.format(ticker,ticker))
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'\s--\sData\s--\s')
    script_data = soup.find('script', text=pattern).contents[0]
    start = script_data.find("context")-2
    json_data = json.loads(script_data[start:-12])
    return json_data
