import json
import re
import copy

from flask import request
from flask_restplus import Resource

from chameleon.utils import db_instance
from chameleon.metrics import QUERIES


class Query(Resource):
    """ return metrics
    """
    def get(self):
        return {'hello': 'world'}

    def post(self):
        """ return [{"target": <name>, "datapoints": [[v,t],[v,t]...]},...]
        """
        data = request.get_json()
        print("JSON: {}".format(data))
        targets_list = data.get('targets')
        time_range = data.get('range')

        metrics_out = list()
        for t in targets_list:
            name = t.get('target')
            if name is None:
                break
            name_pts = name.split('.')
            tartype = t.get('type')
            print("NAME: {}".format(name))
            print("TYPE: {}".format(tartype))
            metric = copy.deepcopy(QUERIES.get(name_pts[0]))
            if len(name_pts) > 1:
                metric = metric.get(name_pts[1])
            if metric:
                query = metric.get('query')
                if query:
                    # need to pass these in to the query if ALL, or subset them
                    args = metric.get('templates')
                    # Template: $source	 templates.metrics.orders_ordered.source
                    # Example: metrics.orders_ordered.source=$source
                    templated = [k for k in args.keys() if k in name]
                    if templated:
                        for k in templated:
                            val = [n for n in name_pts if k in n].pop()
                            val_pts = val.split('=')
                            val_pts[1] = val_pts[1].replace('{', '').replace('}', '')
                            args[val_pts[0]] = tuple(val_pts[1].split(','))
                    args.update(time_range)
                    print('ARGS: {}'.format(args))
                    print('SQL: {}'.format(query))
                    sql_res = db_instance.select(query, args)
                    if tartype == 'timeserie':
                        retval = dict(target=name, datapoints=list())
                        retval['datapoints'] = [[r['val'], r['ts']] for r in sql_res]
                    elif tartype == 'table':
                        retval = dict(columns=list(), rows=list(), type="table")
                        type_lut = {str: "string", int: "number", float: "number"}
                        for c,v in sql_res[0].items():
                            retval['columns'].append(dict(text=c, type=type_lut[type(v)]))
                        retval['rows'] = sql_res[:]
                        print('RES: {}'.format(retval))
                    metrics_out.append(retval)
        return metrics_out

