
from flask import Flask
from retry import retry
from blueprints import loginBlueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@retry(delay=1)
def get_sessionmaker():
	engine = create_engine('postgresql://postgres:postgres@postgres:5432/postgres')
	return sessionmaker(bind=engine)


if __name__ == "__main__":
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'key'

	sessionmaker = get_sessionmaker()

	app.register_blueprint(loginBlueprint.create_blueprint(sessionmaker), url_prefix='/login')
	app.run(debug=True, host='0.0.0.0')