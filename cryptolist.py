# Getting a List of Cryptocurrencies sorted by their most current Market Cap
# (c) 2017 QuantAtRisk.com, by Pawel Lachowicz
# src: http://www.quantatrisk.com/2017/03/20/download-crypto-currency-time-series-portfolio-python/
 
import pandas as pd
import json
from bs4 import BeautifulSoup
import requests
 
url = "https://api.coinmarketcap.com/v1/ticker/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
dic = json.loads(soup.prettify())
 
# create an empty DataFrame
df = pd.DataFrame(columns=["Ticker", "MarketCap"])
 
for i in range(len(dic)):
    df.loc[len(df)] = [dic[i]['symbol'], dic[i]['market_cap_usd']]
 
df.sort_values(by=['MarketCap'])
# apply conversion to numeric as 'df' contains lots of 'None' string as values
df.MarketCap = pd.to_numeric(df.MarketCap)

# print(df.MarketCap)

P = df[df.MarketCap > 20e6]
print(P, end="\n\n")
 
portfolio = list(P.Ticker)
print(portfolio)