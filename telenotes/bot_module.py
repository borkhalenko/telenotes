import telebot
import telenotes.settings as settings

_bot = telebot.TeleBot(settings.bot_settings['TOKEN'])


def start():
    _bot.polling(none_stop=True)


@_bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    answer = ""
    _bot.send_message(message.chat.id, message.text)