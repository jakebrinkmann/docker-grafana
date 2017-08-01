'''
Inspired by: USGS-EROS/espa-api/blob/master/api/util/dbconnect.py (LICENSE NASA-1.3)
'''
import os

import psycopg2
import psycopg2.extras as db_extras

CHAMELEON_PGHOST = os.environ.get('CHAMELEON_PGHOST', 'localhost')
CHAMELEON_PGDB = os.environ.get('CHAMELEON_PGDB', 'postgres')
CHAMELEON_PGTAB = os.environ.get('CHAMELEON_PGTAB', 'postgres')
CHAMELEON_PGUSER = os.environ.get('CHAMELEON_PGUSER', 'postgres')
CHAMELEON_PGPASS = os.environ.get('CHAMELEON_PGPASS', 'postgres')


class DBConnect(object):
    def __init__(self, host=None, dbname=None, user=None, pwrd=None):
        connect_str = ("host={} dbname={} user={} password={}"
                       .format(host or CHAMELEON_PGHOST,
                               dbname or CHAMELEON_PGDB,
                               user or CHAMELEON_PGUSER,
                               pwrd or CHAMELEON_PGPASS))
        print(connect_str)
        conn = psycopg2.connect(connect_str)
        self.cur = conn.cursor(cursor_factory=db_extras.DictCursor)

    def select(self, sql, args, n_records=50):
        sql_log = self.cur.mogrify(sql, args)
        print('SQL LOG: {}'.format(sql_log.decode('utf-8')))
        self.cur.execute(sql, args)
        return self.cur.fetchall()


try:
    db_instance = DBConnect()
except psycopg2.OperationalError as e:
    print('ERR: {}'.format(e))
    db_instance = None

