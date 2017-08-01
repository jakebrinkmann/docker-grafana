import logging

from flask import Flask, request
from flask_restplus import Resource, Api

from .views import Connect, Search, Query, Annotate

app = Flask(__name__)
api = Api(app, doc='/autodocs')

ns = api.namespace('api', description='query database')

ns.add_resource(Connect, '/')
ns.add_resource(Search, '/search')
ns.add_resource(Query, '/query')
ns.add_resource(Annotate, '/annotations')

