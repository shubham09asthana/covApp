from flask_restful import Resource
from flask import request
import logging as log

class Acknowledgement(Resource):
    def post(self):
        df=request.get_json()
        log.info("ACKNOWLEDGEMENT: ",df)
        return 204

class ClusterApplication(Resource):
    def post(self):
        df=request.get_json()
        log.info("MESSAGE From: /ws/v1/cluster/apps/new-application: ",df)
        return 204