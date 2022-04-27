from sqlalchemy import select
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
import flask
from auth.auth_tools import login_required
from database.schema import t_companyhistory


def create_blueprint(Makesession: sessionmaker):
    buySellBlueprint = flask.Blueprint("buySellBlueprint", __name__)

    @buySellBlueprint.route('/', methods=['GET'])
    @login_required(Makesession)
    def getStockDetails():

        session: Session = Makesession()

        res = flask.make_response()
        data = flask.request.args.get('company')

        companyHistory = session.query(t_companyhistory).filter(
            t_companyhistory.columns.company_id == "UBER")

        # companyHistoryQuery = select(t_companyhistory.company_id, t_companyhistory.time_fetched,
        #                              t_companyhistory.trading_price).where(t_companyhistory.company_id == data)
        # companyHistoryQuery = select(t_companyhistory)
        # companyHistory = Session.execute(companyHistoryQuery)

        # companyHistory: list[tuple] = session.query(
        #     t_companyhistory.columns.company_id)

        res = ""
        for s in companyHistory:
            res += s.__repr__() + '\t'

        # print(companyHistory)

        # return companyHistory

        return res

    return buySellBlueprint
