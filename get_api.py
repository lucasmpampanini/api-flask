import requests
from flask import  request

class GetApi:
    """
        Consome API (api.chucknorris.io),
        trata o retorno da API para o formato desejado e 
        retorna o resultado de acordo com o status_code.
    """
    def __init__(self, url):
        self.url = url

    def piada_aleatoria(self):
        """
            Consome API (api.chucknorris.io) e retorna uma piada aleatória
        """

        response = requests.get(self.url)

        if response.status_code == 200:
            retorno = {'results': response.json()['value']}
            return retorno, response.status_code

    def piada_categoria(self, categoria):
        """
            Consome API (api.chucknorris.io) e retorna uma piada aleatória
            de uma categoria especifica
        """
        categoria_api = requests.get('https://api.chucknorris.io/jokes/categories')
        categoria_api = categoria_api.json()

        if categoria in categoria_api:

            response = requests.get(self.url + '?category=' + categoria)

            if response.status_code == 200:
                retorno = {'results': response.json()['value']}
            if response.status_code == 404:
                retorno = {'results': {
                    'code': 404,
                    'message': 'Nenhuma piada encontrada para a categoria ' + categoria,
                    'valid_categories': categoria_api
                }}

            return retorno, response.status_code
        else:
            retorno = {'results': {
                'code': 404,
                'message': 'Nenhuma piada encontrada para a categoria ' + categoria + '. Escolha uma categoria válida.',
                'valid_categories': categoria_api
            }}
            return retorno, 404


    def piada_filtro(self):
        """
            Consome API (api.chucknorris.io) e retorna uma lista de piadas
            de acordo com o filtro de busca e o limite de piadas
        """
        query = request.args.get('search')
        limit = int(request.args.get('limit'))

        response = requests.get(self.url + '?query=' + query)
        
        if response.status_code == 200:
            registros = response.json()['total']

            if registros >= limit:
                resultado = []
                for joke in range(len(response.json()['result'][:limit])):
                    resultado.append(response.json()['result'][joke]['value'])
                
                retorno = {'results': resultado}
                
                return retorno, response.status_code
            else:
                resultado = []
                for joke in range(len(response.json()['result'])):
                    resultado.append(response.json()['result'][joke]['value'])
                
                retorno = {'results': resultado}
                return retorno, response.status_code

        if response.status_code == 404:
            retorno = {'results': {
                'code': 404,
                'message': 'Nenhuma piada encontrada para a busca ' + query
            }}
            return retorno, response.status_code