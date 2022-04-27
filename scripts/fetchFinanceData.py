import signal
import psycopg2
import numpy as np
import pandas as pd
import time
from tqdm import tqdm
from yahoo_fin import stock_info as si

kill_now = False


def signalHandler(sig, frame):
    global kill_now
    kill_now = True


def fetchLoop():

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

    con.commit()
    con.close()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)
    fetchLoop()
