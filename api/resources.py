from database.models.models import User
from flask_restful import Resource
import json


class RestUsers(Resource):
    def get(self):
        users = User.objects()
        user_json = users.to_json()
        return json.loads(user_json)
