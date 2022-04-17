import numpy as np
import pandas as pd
import time
import yfinance as yf


def fetchLoop():

    while True:
        msft = yf.Ticker("MSFT")
        googl = yf.Ticker("GOOGL")
        appl = yf.Ticker("APPL")
        gs = yf.Ticker("GS")
        uber = yf.Ticker("UBER")

        print(msft.history("5m"))

        time.sleep(60*5)


# df.head()


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
