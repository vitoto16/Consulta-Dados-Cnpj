from flask import Flask, jsonify
from flask_restx import Api, Resource
from models import Busca

app = Flask(__name__)
api = Api(app)

app.config['JSON_AS_ASCII'] = False


@api.route('/cnpj/<string:cnpj>')
@api.doc(params={'cnpj': 'Um cnpj válido.'})
class DadosTitular(Resource):
    def get(self, cnpj):
        busca = Busca()
        dados_titular = busca.raspa_dados(cnpj)

        return jsonify(dados_titular)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")