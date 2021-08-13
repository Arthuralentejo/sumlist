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
        contador = 0
        for i in range(size):
            atual = 0
            for j in range(i,size):
                contador+=1
                atual += lista[j]
                if atual > parcial:
                    parcial = atual
                    sequencia = i #"{0}:{1}".format(i,j)
        return {
            "data": lista,
            "result": parcial,
            "contador":contador,
            "best-sequence": sequencia
        }


api.add_resource(Sumtest, '/')
if __name__ == '__main__':
    app.run(debug=True)