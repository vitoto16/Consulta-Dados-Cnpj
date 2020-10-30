from bs4 import BeautifulSoup
import requests


class Busca:
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.base_url = "http://www.portaltransparencia.gov.br/busca/pessoa-juridica/"
        self.dados_titular = dict()

    def __repr__(self):
        return f"Busca({self.cnpj})"

    def raspa_dados(self):
        response_html = requests.get(self.base_url + self.cnpj).text
        soup = BeautifulSoup(response_html, features='lxml')
        section = soup.find('section', class_='dados-tabelados')
        for row in section.children:
            if row.name == 'div':
                for column in row.children:
                    if column.name == 'div' and column.strong:
                        dado = self._trata_string(column.span.text)
                        self.dados_titular[column.strong.text] = dado

    def _trata_string(self, some_string: str):
        new_string = some_string.strip()
        if '\n' in new_string:
            parts = new_string.split('\n')
            for part in range(len(parts)):
                parts[part] = parts[part].strip()
            new_string = ' '.join(parts)

        return new_string
