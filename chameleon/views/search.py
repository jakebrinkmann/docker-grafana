import json

from flask import request
from flask_restplus import Resource

from chameleon.utils import db_instance
from chameleon.metrics import QUERIES

class Search(Resource):
    """ used for find metric
    """
    def get(self):
        return {'hello': 'world'}

    def post(self):
        """ return [{"text": <name>, "value": <n>},...] or [<name>, <name>,...]
        """
        data = request.get_json() # This might be used for templating (.* wildcards)
        print('JSON: {}'.format(data))
        target = data.get('target')
        target_keys = list(QUERIES.keys())
        # Somehow, I want to split these on the '.' and return relevant adaptive queries
        # Support for '*', or "ALL" too?
        if target != 'select metric':
            name_pts = target.split('.')
            if name_pts[0] == 'templates' and len(name_pts) == 4:
                # Example: templates.metrics.orders_ordered.source
                print('NAME: {}'.format(name_pts))
                metric = QUERIES.get(name_pts[1])
                templates = metric.get(name_pts[2]).get('templates')
                print('TEMPLATES: {}'.format(templates))
                target_keys = list(templates.get(name_pts[3]))
                print('KEYS: {}'.format(target_keys))
            elif len(name_pts) == 1:
                target_keys += ['{}.{}'.format(target, k)
                                for k in QUERIES.get(target).keys()]
        return target_keys
