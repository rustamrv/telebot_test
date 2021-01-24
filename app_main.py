from flask import Flask, request
from flask_restful import Api
from api.resources.resources import RestUsers

app = Flask(__name__)
api = Api(app)
api.add_resource(RestUsers, 'api/users')


@app.route('api/index', methods=["GET"])
def index():
    return "Hello world"


@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


app.run()
