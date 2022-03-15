
# DB_NAME = "mysql://root:password@localhost:3306"

import sys
from flask import Flask
from blueprints import loginBlueprint
from database.dbConnect import init_database, execute_query, print_customers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
database = {}


@app.route("/testQuery/<sql>")
def hello(sql):
	db = init_database()
	result = execute_query(db, sql)
	return result


@app.route("/printCustomers")
def printCustomers():
	engine = init_database()
	result = print_customers(engine)
	return result

app.register_blueprint(loginBlueprint.create_blueprint(database), url_prefix='/login')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')