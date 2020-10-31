from bs4 import BeautifulSoup
import requests


class Busca:
    def __init__(self):
        self.base_url = "http://www.portaltransparencia.gov.br/busca/pessoa-juridica/"

    def __repr__(self):
        return f"Busca()"

    # COLETA O HTML DA PAGINA UTILIZANDO A BIBLIOTECA REQUESTS E NAVEGA PELO HTML UTLIZANDO A BIBLIOTECA BEAUTIFULSOUP
    def raspa_dados(self, cnpj):
        dados_titular = dict()
        response_html = requests.get(self.base_url + cnpj).text
        soup = BeautifulSoup(response_html, features='lxml')
        section = soup.find('section', class_='dados-tabelados')
        for row in section.children:
            if row.name == 'div':
                for column in row.children:
                    if column.name == 'div' and column.strong:
                        dado = self._trata_string(column.span.text)
                        dados_titular[str(column.strong.text)] = str(dado)

        return dados_titular

    def _trata_string(self, some_string: str):
        new_string = some_string.strip()
        if '\n' in new_string:
            parts = [part.strip() for part in new_string.split('\n')]
            new_string = ' '.join(parts)

        parts = [part.strip() for part in new_string.split()]
        new_string = ' '.join(parts)

        return new_string
