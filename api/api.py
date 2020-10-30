from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/cnpj/<int:cnpj>')
class DadosTitular(Resource):
    def get(self):

if __name__ == '__main__':
    app.run(Debug=True)