from flask import Blueprint
from restapi.controllers.endpoint_controllers import new_user , new_incident, get_all_incidents, get_one_incident

bprint = Blueprint("endpoint_views",__name__, url_prefix="/api/v1")

@bprint.route('/users', methods=['POST'])
def create_user():
    return new_user()

@bprint.route('/redflags', methods=['POST'])
def create_redflag():
    return new_incident()

@bprint.route('/interventions', methods=['POST'])
def create_incident():
    return new_incident()

@bprint.route('/redflags', methods=['GET'])
def get_all_records():
    return get_all_incidents()

@bprint.route('/redflags/<int:redflagid>', methods=['GET'])
def get_one_records(redflagid):
    return get_one_incident(redflagid)

"""
@bprint.route('/redflag', methods=['POST'])
def create_redflag():
    return add_redflag()

@bprint.route('/intervention', methods=['POST'])
def create_intervention():
    return add_intervention()
"""