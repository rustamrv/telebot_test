from flask import Flask, request, abort
from mongoengine import NotUniqueError
from telebot import TeleBot
from telebot.types import Message
from telebot.types import Update
from bot.config.config import TOKEN, WEBHOOK_URI
from database.models.models import User

app = Flask(__name__)

bot = TeleBot(TOKEN)


@app.route('/')
@app.route('/index')
def index():
    return "Hello world"


@app.route(WEBHOOK_URI, methods=['POST'])
def handler_webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    abort(403)


# Handler commands


@bot.message_handler(commands=['start'])
def handle_start(message: Message):
    try:
        User.objects.create(
            telegram_id=message.chat.id,
            username=getattr(message.from_user, 'username', None),
            first_name=getattr(message.from_user, 'first_name', None)
        )
    except NotUniqueError as err:
        print(err)

    name = f', {message.from_user.first_name}' if getattr(message.from_user, 'first_name') else ''
    greet = f"Hello {name}, i am bot"
    print(greet)
    bot.send_message(message.chat.id, greet)
