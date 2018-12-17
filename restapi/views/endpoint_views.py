from flask import Blueprint
from restapi.controllers.endpoint_controllers import new_user , new_incident,\
    get_all_incidents, get_one_incident, new_comment, new_location, delete_flag, update_status

bprint = Blueprint("endpoint_views",__name__, url_prefix="/api/v1")

@bprint.route('/users', methods=['POST'])
def create_user():
    return new_user()

@bprint.route('/redflags', methods=['POST'])
def create_redflag():
    return new_incident()

@bprint.route('/redflags', methods=['GET'])
def get_all_records():
    return get_all_incidents()

@bprint.route('/redflags/<int:redflagid>', methods=['GET'])
def get_one_records(redflagid):
    return get_one_incident(redflagid)

@bprint.route('/redflags/<int:redflagid>/comment', methods=['PATCH'])
def edit_redflag_comment(redflagid):
    return new_comment(redflagid)

@bprint.route('/redflags/<int:redflagid>/location', methods=['PATCH'])
def edit_redflag_location(redflagid):
    return new_location(redflagid)

@bprint.route('/redflags/<int:redflagid>', methods=['DELETE'])
def delete_redflag_location(redflagid):
    return delete_flag(redflagid)

@bprint.route('/redflags/<int:redflagid>/status', methods=['PATCH'])
def update_flag(redflagid):
    return update_status(redflagid)
