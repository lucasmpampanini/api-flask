from namespaces import api

retorno_piada_aleatoria_200 = api.schema_model('retorno_piada_aleatoria', {
    'type': 'object',
    'properties': {
        'results': {
            'type': 'string',
            'description': 'Piada aleatória do Chuck Norris'
        }
    }
})

retorno_piada_categoria_200 = api.schema_model('retorno_piada_categoria', {
    'type': 'object',
    'properties': {
        'results': {
            'type': 'string',
            'description': 'Piada aleatória do Chuck Norris de uma categoria especifica'
        }
    }
})

retorno_piada_categoria_404 = api.schema_model('retorno_piada_categoria_404', {
    'type': 'object',
    'properties': {
        'results': {
            'properties': {
                'code': {
                    'type': 'integer',
                    'description': 'Código de status da resposta'
                },
                'message': {
                    'type': 'string',
                    'description': 'Mensagem de erro'
                },
                'valid_categories': {
                    'type': 'array',
                    'description': 'Lista de categorias disponíveis',
                    'items': {
                        'type': 'string',
                        'description': 'Categoria'
                    }
                }
            }
        }
    }
})

retorno_piada_filtro_200 = api.schema_model('retorno_piada_filtro', {
    'properties': {
        'results': {
            'type': 'array',
            'description': 'Lista de piadas do Chuck Norris',
            'items': {
                'type': 'string',
                'description': 'Piada do Chuck Norris'
                }
            }
        }
})

retorno_piada_filtro_404 = api.schema_model('retorno_piada_filtro_404', {
    'properties': {
        'results': {
            'properties': {
                'code': {
                    'type': 'integer',
                    'description': 'Código de status da resposta'
                },
                'message': {
                    'type': 'string',
                    'description': 'Mensagem de erro'
                }
            }
        }
    }
})
