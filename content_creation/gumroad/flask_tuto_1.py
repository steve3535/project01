from flask import Flask,app,request
from flask_restful import Api,Resource,reqparse
import time
from typing import List,Dict,Any

APP: app.Flask = Flask(__name__) 
API: Api = Api(APP)
parser = reqparse.RequestParser()
parser.add_argument('id',type=int,help='log identifier')
parser.add_argument('msg',type=str,help='log message')

LOGS: List[Dict[str,any]] = [
        {
            "timestamp": time.time(),
            "msg": "Log message 1"
            },
        {
            "timestamp": time.time(),
            "msg": "Log message 2"
            }
        ]

class MyLogs(Resource):
    def get(self):
        return LOGS

class MyLog(Resource):
    def get(self):
       args = parser.parse_args() 
       if args['id'] is None or args['id']>len(LOGS):
           return 'unknown Log ID',400
       return LOGS[args['id']-1]

    def put(self):
       args = parser.parse_args()
       if args['msg'] is None:
           return 'BE SERIOUS',400
       LOGS.append({"timestamp":time.time(),"msg":args['msg']})
       return "New Log added",201

API.add_resource(MyLogs,'/logs')
API.add_resource(MyLog,'/log')

if __name__ == '__main__':
    APP.run(debug='true',port='9990')


