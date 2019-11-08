from telegram.ext import Updater, CommandHandler
import telenotes.settings as settings


def hello(update, context):
    update.message.reply_text("Hello {}".format(update.message.from_user.first_name))

def start(update, context):
    update.message.reply_text("Started...")

def start():
    _updater = Updater(settings.bot_settings['TOKEN'], use_context=True)
    _updater.dispatcher.add_handler(CommandHandler('hello', hello))
    _updater.dispatcher.add_handler(CommandHandler('start', start))
    _updater.start_polling()
    _updater.idle()
