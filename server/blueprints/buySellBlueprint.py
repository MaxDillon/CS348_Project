from sqlalchemy import false, select
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
import flask
from auth.auth_tools import login_required
from database.schema import Company, Fundinfo, t_companyhistory

# TODO:
# [] update stocks owned if buying/selling
# [*] write condition for when selling
# [] create new transaction


def getCurrentShareprice(session: Session, company: str) -> int:
    # Get last fetched time
    ts = session.execute(
        session.query(sqlalchemy.func.max(
            t_companyhistory.columns.time_fetched)
        )
        .filter(t_companyhistory.columns.company_id == company)
    ).one()[0]

    # Check the value of a share in the market now
    stockPriceQuery = session.query(t_companyhistory.columns.trading_price)\
        .filter(t_companyhistory.columns.company_id == company)\
        .filter(t_companyhistory.columns.time_fetched == ts)

    stockPrice = session.execute(stockPriceQuery).one()[0]

    return stockPrice


def getFundvalue(session: Session):
    # with_for_update() sets update lock:
    # https://dev.to/ivankwongtszfung/safe-update-operation-in-postgresql-using-sqlalchemy-3ela

    fundValueQuery = session.query(
        Fundinfo.fund_value).with_for_update()
    fundValue = session.execute(fundValueQuery).one()\
        ._asdict()['fund_value']

    return fundValue


def getSharesOwned(session: Session, company: str) -> int:
    sharesOwnedQuery = session.query(Company.num_shares).filter(
        Company.company_id == company)

    sharesOwned = session.execute(sharesOwnedQuery).one()[0]
    return sharesOwned


def create_blueprint(Makesession: sessionmaker):
    buySellBlueprint = flask.Blueprint("buySellBlueprint", __name__)

    @buySellBlueprint.route('/', methods=['GET'])
    @login_required(Makesession)
    def getStockDetails():

        response_body = {
            "error": None,
            "data": None
        }

        session: Session = Makesession()
        companyID: str = flask.request.args.get('company')

        if companyID == None or companyID == "":
            response_body["error"] = "No company name passed"
            res = flask.make_response(flask.jsonify(response_body), 400)
            return res

        companyID = companyID.upper()  # All company ids are in uppercase

        companyHistoryQuery = session.query(t_companyhistory.columns.time_fetched, t_companyhistory.columns.trading_price).filter(
            t_companyhistory.columns.company_id == companyID)

        companyHistory = session.execute(companyHistoryQuery).all()

        response = [x._asdict() for x in companyHistory]

        companyDetailsQuery = session.query(
            Company.company_name, Company.num_shares).filter(Company.company_id == companyID)

        companyDetails = session.execute(companyDetailsQuery).one()

        session.close()

        # response: {time_fetched:int, trading_price:str}[]

        response_body["data"] = {
            "stockData": response,
            "companyDetails": companyDetails._asdict()
        }

        res = flask.make_response(flask.jsonify(response_body), 200)
        return res

    @buySellBlueprint.route('/', methods=['POST'])
    @login_required(Makesession)
    def executeTransaction():
        response_body = {
            "error": None,
            "data": None
        }

        session: Session = Makesession()

        reqBody = flask.request.get_json(silent=True)

        if (reqBody == None):
            response_body["error"] = "Malformed body"
            res = flask.make_response(flask.jsonify(response_body), 400)
            return res

        if (reqBody == {}):
            response_body["error"] = "Empty body"
            res = flask.make_response(flask.jsonify(response_body), 400)
            return res

        # Cleaning the request
        reqBody["company"] = reqBody["company"].upper()
        reqBody["value"] = int(reqBody["value"])

        # Check our cash floating
        fundValue = getFundvalue()
        print("fundvalue: ", fundValue, flush=True)

        # Check the value of a shares
        stockPrice = getCurrentShareprice(session, reqBody["company"])
        print("stock price: ", stockPrice, flush=True)

        # Get number of shares owned
        sharesOwned = getSharesOwned(session, reqBody["company"])
        print("shares owned: ", sharesOwned, flush=True)

        if reqBody["buy"] == True:

            # Check if our floating cash is more than the transaction cost
            if fundValue < stockPrice * reqBody["value"]:
                response_body["error"] = "Insufficient funds"
                res = flask.make_response(flask.jsonify(response_body), 400)
                return res

            # Updates the floating cash
            fundValue -= stockPrice * reqBody["value"]

            # Updates the number of shares owned
            sharesOwned += reqBody["value"]

            response_body["data"] = {
                "message": f"Successfuly bought {reqBody['value']} shares of {reqBody['company']}"
            }

        else:
            # Check if we have enough stocks for that company
            if sharesOwned < reqBody["value"]:
                response_body["error"] = "Insufficient shares owned"
                res = flask.make_response(flask.jsonify(response_body), 400)
                return res

            sharesOwned -= reqBody["value"]
            fundValue += stockPrice * reqBody["value"]

            response_body["data"] = {
                "message": f"Successfuly sold {reqBody['value']} shares of {reqBody['company']}"
            }

        # Update the stocks owned
        session.query()

        session.commit()
        session.close()

        res = flask.make_response(flask.jsonify(response_body), 200)

        return res

    return buySellBlueprint
