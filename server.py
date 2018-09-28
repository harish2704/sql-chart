import falcon
import sqlalchemy
import json
import sys
import datetime
import os

db_url = os.environ[ 'DB_CONNECTION' ] if 'DB_CONNECTION' in os.environ else 'postgresql://postgres@localhost/postgres'
eng = sqlalchemy.create_engine(db_url, pool_size=1, pool_recycle=3600)
conn = eng.connect()
print "Connected to db"

class QResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        sql = req.params['q']
        result = conn.execute(sql)
        data = [(dict(row.items())) for row in result]
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        resp.set_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        resp.set_header('content-type', 'application/json; charset=UTF-8')
        resp.body = json.dumps( data, default=str )

api = falcon.API()
api.add_static_route('/', os.path.dirname(os.path.realpath(__file__)) + '/static' )
api.add_route('/api/data', QResource())
