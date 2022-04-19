# %%
from datetime import datetime
import psycopg2
import numpy as np
import pandas as pd
import time
from tqdm import tqdm
from yahoo_fin import stock_info as si
import datetime
# import requests

#  sudo service postgresql start

# API_KEY = """4VCCJ8MVXHVCNL14"""

# # %%

# company = 'AMZN'
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&apikey={API_KEY}'
# r = requests.get(url)
# data = r.json()

# print(data)

# # %%

# datetime.strptime('2022-04-14 20:00:00', '%Y-%m-%d %H:%M:%S')

# %%


def fetchLoop():

    stocks = ["MSFT", "GOOGL", "AMZN", "GS", "UBER"]

    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="postgres",
        port="5432",
    )

    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS CompanyHistory (
            company_id varchar(250),
            time_fetched TIMESTAMP NOT NULL,
            trading_price MONEY NOT NULL
            );"""
    )

    for i in tqdm(range(10)):
        current_prices = {}

        for stock in stocks:
            current_prices[stock] = si.get_live_price(stock)

        query = f"""INSERT INTO CompanyHistory(company_id, time_fetched, trading_price) VALUES (%s, %s, %s)"""

        for stock in stocks:
            cur.execute(
                query, (stock, datetime.datetime.now(), current_prices[stock]))

        con.commit()

        time.sleep(60)

    cur.execute("Select * from CompanyHistory")

    for row in cur.fetchall():
        print(row)

    con.commit()
    con.close()


if __name__ == "__main__":
    fetchLoop()


# # %%
# # %%
# fig = go.Figure(data=[
#     go.Candlestick(
#         x=list(df.index),
#         open=df.Open,
#         close=df.Close,
#         high=df.High,
#         low=df.Low
#     )
# ])

# fig.update_xaxes(

#     rangeslider_visible=True,
#     rangebreaks=[
#         # NOTE: Below values are bound (not single values), ie. hide x to y
#         # hide weekends, eg. hide sat to before mon
#         dict(bounds=["sat", "mon"]),
#         # hide hours outside of 9.30am-4pm
#         # dict(bounds=[16, 9.5], pattern="hour"),
#         # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
#     ],
#     # rangeselector=dict(
#     #     buttons=list([
#     #         dict(count=1,
#     #                  label="1m",
#     #                  step="month",
#     #                  stepmode="backward"),
#     #         dict(count=6,
#     #              label="6m",
#     #              step="month",
#     #              stepmode="backward"),
#     #         dict(count=1,
#     #              label="YTD",
#     #              step="year",
#     #              stepmode="todate"),
#     #         dict(count=1,
#     #              label="1y",
#     #              step="year",
#     #              stepmode="backward"),
#     #         dict(step="all")
#     #     ])
#     # )

# )


# fig.update_layout(xaxis_rangeslider_visible=False)

# fig.show()
