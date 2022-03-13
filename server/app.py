
# DB_NAME = "mysql://root:password@localhost:3306"

from flask import Flask
from blueprints.loginPage import loginPage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.register_blueprint(loginPage, url_prefix='/login')


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')