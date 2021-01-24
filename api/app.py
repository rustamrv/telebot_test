from flask import Flask
from flask_restful import Api
from api.resources.resources import RestUsers

app = Flask(__name__)
api = Api(app)
api.add_resource(RestUsers, '/users')


@app.route('/')
def index():
    return "Hello world"
