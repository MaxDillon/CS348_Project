
from datetime import datetime
from flask import Blueprint

loginPage = Blueprint('loginPage', __name__)


@loginPage.route('/getDate', methods=['GET'])
def getDate():
	now = datetime.now()
	return {
		'date': now
	}