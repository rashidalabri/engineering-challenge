import json

from flask import Flask, escape, request, jsonify, abort
from flask_restful import Resource, Api, reqparse

import resources

# TODO: Implement local and server-side caching


app = Flask(__name__)
api = Api(app)

api.add_resource(resources.CharacterList, '/characters')
api.add_resource(resources.Character, '/characters/<string:id>')

@app.route('/')
def index():
    return {}

@app.errorhandler(400)
def resource_does_not_exist(error):
    response = jsonify({'message': error['message']})
    return response