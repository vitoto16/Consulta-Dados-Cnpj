from bs4 import BeautifulSoup
import requests

class Busca:
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.base_url = "http://www.portaltransparencia.gov.br/busca/pessoa-juridica/"

    def __repr__(self):
        return f"Busca({self.cnpj})"

    def busca_dados(self):
        response = requests.get(self.base_url+cnpj, features='lxml')
        response_html = response.text
        soup = BeautifulSoup(response_html)