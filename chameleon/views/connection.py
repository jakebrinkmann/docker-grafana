from flask_restplus import Resource, abort

from chameleon.utils import db_instance

class Connect(Resource):
    """ used for test connection
    """
    def get(self):
        if db_instance is None:
            abort(500, 'Could not connect database')
        else:
            return 'ok'

