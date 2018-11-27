from flask import Blueprint
from restapi.controllers.endpoint_controllers import new_user , new_incident

bprint = Blueprint("endpoint_views",__name__, url_prefix="/api/v1")

@bprint.route('/users', methods=['POST'])
def create_user():
    return new_user()

@bprint.route('/redflag', methods=['POST'])
def create_incident():
    return new_incident()

"""
@bprint.route('/redflag', methods=['POST'])
def create_redflag():
    return add_redflag()

@bprint.route('/intervention', methods=['POST'])
def create_intervention():
    return add_intervention()
"""