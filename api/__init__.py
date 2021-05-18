import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api
from app import flaskAppInstance
from .covapp import CovApp
from .additionals import ClusterApplication,Acknowledgement


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(CovApp,"/sms")

restServerInstance.add_resource(Acknowledgement,"/got")

restServerInstance.add_resource(ClusterApplication,"/ws/v1/cluster/apps/new-application")

##TO DO
'''
    1. Receiver class for server's acknowledgement
    2. Recevier class for default health check
'''