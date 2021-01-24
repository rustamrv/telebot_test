from flask import Flask
from flask_restful import Api
from api.resources.resources import RestUsers

app = Flask(__name__)
api = Api(app)
api.add_resource(RestUsers, '/users')


@app.route('/index')
def index():
    return "Hello world"
