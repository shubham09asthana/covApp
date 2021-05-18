import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api
from app import flaskAppInstance
from .covapp import CovApp



restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(CovApp,"/sms")

##TO DO
'''
    1. Receiver class for server's acknowledgement
    2. Recevier class for default health check
'''