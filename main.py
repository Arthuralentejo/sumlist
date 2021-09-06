#!/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Sumtest(Resource):
    def post(self):
        lista = json.loads(request.data)['list']
        result = 0
        size = len(lista)
        for i in range(size):
            current = 0
            for j in range(i,size):
                current += lista[j]
                if current > result:
                    result = current
        return {
            "List": lista,
            "result": result
        }

api.add_resource(Sumtest, '/maxsum/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)