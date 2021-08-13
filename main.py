from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Sumtest(Resource):
    def post(self):
        dados = json.loads(request.data)
        lista = dados['list']
        sequencia = ""
        parcial = 0
        size = len(lista)
        for i in range(size):
            atual = 0
            for j in range(i,size):
                atual += lista[i]
                if parcial < atual:
                    parcial = atual
                    sequencia = "{}:{}".format(i,j)
        return {
            "data": lista,
            "result": parcial,
            "best-sequence": sequencia
        }


api.add_resource(Sumtest, '/')
if __name__ == '__main__':
    app.run(debug=True)