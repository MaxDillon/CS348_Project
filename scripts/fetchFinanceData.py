import signal
import psycopg2
import time
from yahoo_fin import stock_info as si
import datetime

con = None
cur = None


def signalHandler(sig, frame):
    global con, cur

    if cur:
        cur.close()

    if con:
        con.commit()
        con.close()

    exit(0)


def marketOpen():
    currentTime = datetime.datetime.now().time()

    start = datetime.time(9, 30, 0)
    end = datetime.time(16, 30, 0)

    return start <= currentTime <= end


def fetchLoop():
    global con
    global cur

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

    while True:

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


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)
    fetchLoop()
