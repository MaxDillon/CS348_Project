
from flask import Flask
from retry import retry
from blueprints import authBlueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from scripts.fetchFinanceData import fetchLoop


@retry(delay=1)
def get_sessionmaker():
    engine = create_engine(
        'postgresql://postgres:postgres@postgres:5432/postgres')
    return sessionmaker(bind=engine)


if __name__ == "__main__":

    fetchLoop()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'

    sessionmaker = get_sessionmaker()

    app.register_blueprint(authBlueprint.create_blueprint(
        sessionmaker), url_prefix='/auth')
    app.run(debug=True, host='0.0.0.0')
