from telegram.ext import Updater
import requests

BOT_Token="5060205265:AAEKUdFBoz_ADOJiOkRHtIGLDyHU4mT_rAQ"
updater = Updater(BOT_Token)

def incoming_message_action(update, context):
  image_url=requests.post('https://single-developers.herokuapp.com/write', headers={'Content-Type': 'application/json'}, json={"text":f"{update.message.text}"}).history[1].url
  context.bot.sendPhoto(chat_id=update.message.chat.id, photo=image_url,
                          reply_to_message_id=update.message.reply_to_message.message_id)

updater.dispatcher.add_handler( MessageHandler(Filters.text, incoming_message_action))
updater.start_polling()
updater.idle()