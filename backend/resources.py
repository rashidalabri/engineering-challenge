from flask import abort
from flask_restful import Resource, reqparse

import models, parsers, config


character_model = models.Character()

class ModelResource(Resource):

    model = None

    def get(self, id):
        if not self.model.exists(id):
            abort(404, 'Resource does not exist.')
        return self.model.get(id)


class ModelListResource(Resource):

    model = None

    def get(self, limit = config.PAGINATION_MAX_ELEMS_PER_PAGE):
        args = parsers.pagination_parser.parse_args()
        results = self.model.all()[limit * (args['page'] - 1) : limit * args['page']]
        return {
            'count': len(self.model.all()),
            'page': args['page'],
            'next': len(self.model.all()) > limit * args['page'],
            'previous': args['page'] > 1,
            'results': results
        }


class CharacterResource(ModelResource):
    model = character_model


class CharacterListResource(ModelListResource):
    model = character_model

