import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import json


def get_attributes(stocks, df):
    for i in range(len(stocks)):
        stocks[i].eps = df.loc[i, "EPS"]
        stocks[i].growth = df.loc[i, "Growth"]
        stocks[i].pe_ratio = df.loc[i, "P/E"]
        stocks[i].fair_val = df.loc[i, "Fair"]
        stocks[i].moving50 = df.loc[i, "Moving50"]
        stocks[i].moving200 = df.loc[i, "Moving200"]


def get_json(url, ticker):
    response = requests.get(url.format(ticker, ticker))
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'\s--\sData\s--\s')
    script_data = soup.find('script', text=pattern).contents[0]
    start = script_data.find("context") - 2
    json_data = json.loads(script_data[start:-12])

    return json_data
