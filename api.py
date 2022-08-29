from flask import Flask
from flask_restplus import Resource
from get_api import GetApi
from namespaces import ns1, api, app
from model_swagger import retorno_piada_aleatoria_200,\
    retorno_piada_categoria_200, retorno_piada_categoria_404,\
    retorno_piada_filtro_200, retorno_piada_filtro_404


@ns1.route('/random')
class PiadaAleatoria(Resource):
    @api.response(200, 'Piada enviada com sucesso!', retorno_piada_aleatoria_200)
    def get(self):
        """
            Retorna uma piada aleatória
        """
        api = GetApi('https://api.chucknorris.io/jokes/random')
        retorno = api.piada_aleatoria()
        return retorno

@ns1.route('/random/category/<CATEGORIA>')
class PiadaCategoria(Resource):
    @api.response(200, 'Piada por categoria enviada com sucesso!', retorno_piada_categoria_200)
    @api.response(404, 'Nenhuma piada encontrada para a categoria enviada!', retorno_piada_categoria_404)
    def get(self, CATEGORIA):
        """
            Escolha uma categoria para retornar uma piada aleatória
        """
        api = GetApi('https://api.chucknorris.io/jokes/random')
        retorno = api.piada_categoria(CATEGORIA)
        return retorno

@ns1.route('/filter')
@api.param('search', 'Filtro de busca', type=str, required=True)
@api.param('limit', 'Limite de piadas', type=int, required=True)
class PiadaFiltro(Resource):
    @api.response(200, 'Piadas filtradas com sucesso!', retorno_piada_filtro_200)
    @api.response(404, 'Nenhuma piada encontrada para o filtro de busca!', retorno_piada_filtro_404)
    def get(self):
        """
            Digite uma palavra chave para filtrar as piadas
        """
        api = GetApi('https://api.chucknorris.io/jokes/search')
        retorno = api.piada_filtro()
        return retorno

if __name__ == '__main__':
    app.run(debug=True)
