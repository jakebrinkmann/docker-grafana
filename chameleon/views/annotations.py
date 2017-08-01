import json

from flask import request
from flask_restplus import Resource

from chameleon.utils import db_instance

class Annotate(Resource):
    """ return annotations
    """
    def get(self):
        return {'hello': 'world'}

    def post(self):
        data = request.get_json()
        print(data)
        return [
  {
    "annotation": {
      "name": "annotation name", #should match the annotation name in grafana
      "enabled": True,
      "datasource": "generic datasource",
     },
    "title": "Cluster outage",
    "time": 1493754891090,
    "text": "Joe causes brain split",
    "tags": "joe, cluster, failure"
  }
]
