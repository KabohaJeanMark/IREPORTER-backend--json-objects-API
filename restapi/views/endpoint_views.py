from flask import Blueprint
from restapi.controllers.endpoint_controllers import new_user

bprint = Blueprint("endpoint_views",__name__, url_prefix="/api/v1")

@bprint.route('/users', methods=['POST'])
def create_user():
    return new_user()