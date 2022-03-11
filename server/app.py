from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
	now = datetime.now()
	return {
		"date": str(now)
	}


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')