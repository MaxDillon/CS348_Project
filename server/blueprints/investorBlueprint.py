from flask import Blueprint, make_response, redirect, request
from blueprints.loginBlueprint import login_required


def create_blueprint(database):
    investorBlueprint = Blueprint('investorBlueprint', __name__)

    @investorBlueprint.route('/detials', methods=['GET'])
    @login_required(database)
    def getInvestorDetails():
        resp = make_response()
        data = request.get_json()

        username = request.get('username')
