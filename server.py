#!/usr/bin/env python3
import falcon
import sqlalchemy
import json
from sqlalchemy import text
import os

db_url = os.environ[ 'DB_CONNECTION' ] if 'DB_CONNECTION' in os.environ else 'postgresql://postgres@localhost/postgres'
eng = sqlalchemy.create_engine(db_url, pool_recycle=3600)
conn = eng.connect()
print("Connected to db")

class QResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        sql = req.params['q']
        result = conn.execute(text(sql))
        # __import__('ipdb').set_trace()
        data = [row._asdict() for row in result]
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        resp.set_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        resp.set_header('content-type', 'application/json; charset=UTF-8')
        resp.text = json.dumps( data, default=str )


class RedirectingResource:
    def on_get(self, req, resp):
        raise falcon.HTTPMovedPermanently('/index.html')

api = falcon.API()
api.add_route('/', RedirectingResource())
api.add_static_route('/', os.path.dirname(os.path.realpath(__file__)) + '/static' )
api.add_route('/api/data', QResource())


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')
        # Serve until process is killed
        httpd.serve_forever()
