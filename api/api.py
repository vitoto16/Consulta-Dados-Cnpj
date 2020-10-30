from flask import Flask, jsonify
from flask_restx import Api, Resource
from models import Busca

app = Flask(__name__)
api = Api(app)

app.config['JSON_AS_ASCII'] = False

@api.route('/cnpj/<string:cnpj>')
class DadosTitular(Resource):
    def get(self, cnpj):
        busca = Busca(cnpj)
        busca.raspa_dados()

        return jsonify(busca.dados_titular)

if __name__ == '__main__':
    app.run(debug=True)