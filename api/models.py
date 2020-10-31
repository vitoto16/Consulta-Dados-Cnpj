from bs4 import BeautifulSoup
import requests


class Busca:
    def __init__(self):
        self.base_url = "http://www.portaltransparencia.gov.br/busca/pessoa-juridica/"

    def __repr__(self):
        return "Busca()"

    # COLETA O HTML DA PAGINA UTILIZANDO A BIBLIOTECA REQUESTS E NAVEGA PELO HTML UTLIZANDO A BIBLIOTECA BEAUTIFULSOUP
    def raspa_dados(self, cnpj):
        """Método para raspagem de dados provenientes da página Portal da Transparência. Busca no html pela tag
        'section' com classe 'dados-tabelados'. Em seguida, desce pela árvore da tag e filtra até encontrar as colunas
        onde se encontram os dados. Então, formata o dado encontrado e adiciona a descrição do dado como chave e o dado
        em si como valor em dados_titular. Retorna o dicionário dados_titular."""
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

    @staticmethod
    def _trata_string(some_string: str):
        """Método privado que formata a string passada como parâmetro, retirando espaços em branco e eventuais quebras
        de linha. Retorna a string formatada."""
        new_string = some_string.strip()
        if '\n' in new_string:
            parts = [part.strip() for part in new_string.split('\n')]
            new_string = ' '.join(parts)

        parts = [part.strip() for part in new_string.split()]
        new_string = ' '.join(parts)

        return new_string
