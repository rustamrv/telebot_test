from flask import Blueprint, Flask, redirect, url_for, request
from flask_restful import Api
from resources import RestUsers

app = Flask(__name__)
api = Api(app)
api.add_resource(RestUsers, '/users')


@app.route('/')
def index():
    return "Hello world"
