from sqlalchemy import select
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
import flask
from auth.auth_tools import login_required
from database.schema import Company, t_companyhistory
# from plotly.offline import plot
# from plotly.graph_objs import Scatter


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
            "ok": False
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

        # Check if we have cash floating
        enoughMoney = False

        if (enoughMoney):
            response_body["ok"] = True
            res = flask.make_response(flask.jsonify(response_body), 200)
            return res
        else:
            response_body["error"] = "Insufficient funds"
            res = flask.make_response(flask.jsonify(response_body), 400)
            return res

    return buySellBlueprint
