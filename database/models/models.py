import mongoengine as me


class User(me.Document):
    telegram_id = me.IntField(primary_key=True)
    username = me.StringField(min_length=2, max_lenght=128)
    first_name = me.StringField(min_length=2, max_lenght=128)
