from telegram.ext import Updater
import requests

BOT_Token="7853451df5:SDSGHghjgjdsfgtyY0PXugoowhNL03vyI7w"
updater = Updater(BOT_Token)

def incoming_message_action(update, context):
  image_url=requests.get('https://single-developers.herokuapp.com/logo?name='+(update.message.text).replace(' ','%20'))
  context.bot.sendPhoto(chat_id=update.message.chat.id, photo=image_url,
                          reply_to_message_id=update.message.reply_to_message.message_id)

updater.dispatcher.add_handler( MessageHandler(Filters.text, incoming_message_action))
updater.start_polling()
updater.idle()