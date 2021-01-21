from bot.main_bot import bot
import time
from bot.config.config import WEBHOOK_URL


bot.remove_webhook()
time.sleep(0.5)
bot.set_webhook(WEBHOOK_URL, certificate=open('webhook_cert.pem'))
#bot.polling()