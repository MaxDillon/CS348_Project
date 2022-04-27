# %%
import signal
import psycopg2
import numpy as np
import pandas as pd
import time
from tqdm import tqdm
from yahoo_fin import stock_info as si
import datetime
from zoneinfo import ZoneInfo

kill_now = False


def signalHandler(sig, frame):
    global kill_now
    kill_now = True


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

    print("booting up")

    query = f"""SELECT company_id FROM Company"""
    cur.execute(query)

    stocks = []
    for row in cur.fetchall():
        stocks.append(row[0])

    print("stocks: ", stocks)

    while not kill_now:
        # try:
        current_prices = {}

        for stock in stocks:
            current_prices[stock] = si.get_live_price(stock)

        query = f"""INSERT INTO CompanyHistory(company_id, time_fetched, trading_price) VALUES (%s, %s, %s)"""
        updateCompanyQuery = f"""UPDATE Company SET current_trading_price = %s WHERE company_id = %s"""

        current_time = int(time.time())

        print("time:\t", current_time)

        for stock in stocks:
            cur.execute(
                query, (stock, current_time, current_prices[stock])
            )

            cur.execute(
                updateCompanyQuery, (current_prices[stock], stock)
            )

        con.commit()

        time.sleep(60)
        # except KeyboardInterrupt:
        #     con.commit()
        #     con.close()
        #     break


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)
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
