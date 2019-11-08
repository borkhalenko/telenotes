import telebot
import telegram
import telegram.ext
import telenotes.settings as ts

#https://python-telegram-bot.org/
class TelenotesBot:
    #_bot = telebot.TeleBot(ts.bot_settings['TOKEN'])
    '''
    def __init__(self, settings):
        self._bot = telebot.TeleBot(settings['TOKEN'])

    def start(self):
        self._bot.polling(none_stop=True)

#    @_bot.message_handler(content_types=['text'])
    def repeat_all_messages(self, message):
        self._bot.send_message(message.chat.id, message.text)
    '''
    updater = telegram.ext.Updater(ts.bot_settings['TOKEN'], use_context=True)
    print(bot.get_me())