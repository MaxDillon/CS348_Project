import signal
import psycopg2
import time
from yahoo_fin import stock_info as si
import datetime
import retry

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
    if datetime.datetime.today().weekday() in (5, 6):
        # https://stackoverflow.com/a/29384769/17005788
        return False

    currentTime = datetime.datetime.now().time()

    # datetime.tzinfo.

    print(currentTime)

    start = datetime.time(9, 30, 0)
    end = datetime.time(16, 30, 0)

    return start <= currentTime <= end


@retry.retry(delay=1, tries=5, backoff=2)
def connectToPostgres():
    return psycopg2.connect(
        'postgresql://postgres:postgres@postgres:5432/postgres')


def fetchLoop():
    global con
    global cur

    con = None

    try:
        con = connectToPostgres()
    except Exception as e:
        raise e

    cur = con.cursor()

    print("booting up")

    query = f"""SELECT company_id FROM Company"""
    cur.execute(query)

    stocks = []
    for row in cur.fetchall():
        stocks.append(row[0])

    print("stocks: ", stocks)

    while True:

        if marketOpen():

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
        else:
            print("Market closed")

        time.sleep(60)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)
    fetchLoop()
