from flask import Flask
from restapi.views import endpoint_views

app = Flask(__name__, instance_relative_config = True)
app.register_blueprint(endpoint_views.bprint)