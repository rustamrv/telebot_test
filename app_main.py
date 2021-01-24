from flask import Flask
from flask_restful import Api
from api.resources.resources import RestUsers
from bot.main_bot import bot, app

# app = Flask(__name__)
api = Api(app)
api.add_resource(RestUsers, '/users')


@app.route('/index')
def index():
    return "Hello world"


app.run()
