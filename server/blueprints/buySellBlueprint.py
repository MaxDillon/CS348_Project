from sqlalchemy import select
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
import flask
from auth.auth_tools import login_required
from database.schema import t_companyhistory
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
        companyName: str = flask.request.args.get('company')

        if companyName == None or companyName == "":
            response_body["error"] = "No company name passed"
            res = flask.make_response(flask.jsonify(response_body), 400)
            return res

        companyName = companyName.upper()  # All company ids are in uppercase

        companyHistoryQuery = session.query(t_companyhistory.columns.time_fetched, t_companyhistory.columns.trading_price).filter(
            t_companyhistory.columns.company_id == companyName)

        companyHistory = session.execute(companyHistoryQuery).all()

        response = [x._asdict() for x in companyHistory]

        # response: {time_fetched:int, trading_price:str}[]

        response_body["data"] = response

        res = flask.make_response(flask.jsonify(response_body), 200)
        return res

    return buySellBlueprint
