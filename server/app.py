from flask import Flask
from retry import retry
from blueprints import authBlueprint, transactionBlueprint, buySellBlueprint, editBlueprint, fundInfoBlueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@retry(delay=1)
def get_sessionmaker():
    engine = create_engine(
        "postgresql://postgres:postgres@postgres:5432/postgres")
    return sessionmaker(bind=engine)


if __name__ == "__main__":

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "key"

    # app.register_blueprint(authBlueprint.create_blueprint(sessionmaker), url_prefix='/auth')
    # app.register_blueprint(transactionBlueprint.create_blueprint(sessionmaker), url_prefix='/transactions')
    # app.run(debug=True, host='0.0.0.0')
    sessionmaker = get_sessionmaker()

    app.register_blueprint(authBlueprint.create_blueprint(
        sessionmaker), url_prefix='/auth')

    app.register_blueprint(transactionBlueprint.create_blueprint(
        sessionmaker), url_prefix='/transactions')

    app.register_blueprint(buySellBlueprint.create_blueprint(
        sessionmaker), url_prefix='/buySell')

    app.register_blueprint(
        editBlueprint.create_blueprint(sessionmaker), url_prefix="/edit"
    )

    app.register_blueprint(fundInfoBlueprint.create_blueprint(
        sessionmaker), url_prefix="/fundInfo")

    app.run(debug=True, host="0.0.0.0")
