# Consulta de CNPJ

Simples API construída utilizando flask (flask-restx) com o objetivo de fornecer dados sobre o titular de um CNPJ.

A API recebe o CNPJ que se deseja consultar através da rota `/cnpj/00000000000000`. Então, acessa o Portal da
Transparência, raspa os dados lá expostos e retorna em formato `JSON` a descrição e o valor de cada dado.

### Como utilizar

Para utilizar a versão mais recente via Docker, execute o comando:
`docker run -d -p 5000:5000 vitoto16/dados_cnpj`

Exemplo de consulta: `http://localhost:5000/cnpj/57930950000132`