from unittest import TestCase
from api.models import Busca


class TesteBusca(TestCase):

    def setUp(self):
        self.busca = Busca()
        self.dados_titular = self.busca.raspa_dados("14058693000188")

    def test_deve_retornar_dicionario_populado_de_dados_quando_dado_eh_encontrado_no_site_raspado(self):
        self.assertNotEqual(0, len(self.dados_titular))

    def test_deve_retornar_chave_e_valor_de_bairro_distrito_formatado_quando_raspando_dados(self):
        chave_esperada = "Bairro/Distrito"
        valor_esperado = "CENTRO"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_CNAE_formatado_quando_raspando_dados(self):
        chave_esperada = "CNAE"
        valor_esperado = "47717 - Comércio varejista de produtos farmacêuticos para uso humano e veterinário"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_complemento_formatado_quando_raspando_dados(self):
        chave_esperada = "Complemento"
        valor_esperado = "SALA B"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_data_de_abertura_formatado_quando_raspando_dados(self):
        chave_esperada = "Data de abertura"
        valor_esperado = "29/07/2011"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_endereco_eletronico_formatado_quando_raspando_dados(self):
        chave_esperada = "Endereço eletrônico"
        valor_esperado = "BRASILPOPULARIRATI@YAHOO.COM.BR"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_logradouro_formatado_quando_raspando_dados(self):
        chave_esperada = "Logradouro"
        valor_esperado = "R 19 DE DEZEMBRO"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_municipio_formatado_quando_raspando_dados(self):
        chave_esperada = "Município"
        valor_esperado = "IRATI"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_natureza_juridica_formatado_quando_raspando_dados(self):
        chave_esperada = "Natureza jurídica"
        valor_esperado = "2305 - Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_nome_de_fantasia_formatado_quando_raspando_dados(self):
        chave_esperada = "Nome de fantasia"
        valor_esperado = "H D FARMA"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_nome_empresarial_formatado_quando_raspando_dados(self):
        chave_esperada = "Nome empresarial"
        valor_esperado = "H & D FARMA EIRELI"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_numero_formatado_quando_raspando_dados(self):
        chave_esperada = "Número"
        valor_esperado = "639"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_numero_de_inscricao_separado_apenas_por_espaco_quando_raspando_dados(self):
        valor_esperado = "14.058.693/0001-88 MATRIZ"

        self.assertEqual(valor_esperado, self.dados_titular['Número de inscrição'])

    def test_deve_retornar_chave_e_valor_de_telefone_formatado_quando_raspando_dados(self):
        chave_esperada = "Telefone"
        valor_esperado = "42 31322388 42 31322388"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])

    def test_deve_retornar_chave_e_valor_de_uf_formatado_quando_raspando_dados(self):
        chave_esperada = "UF"
        valor_esperado = "PR"

        self.assertEqual(valor_esperado, self.dados_titular[chave_esperada])
