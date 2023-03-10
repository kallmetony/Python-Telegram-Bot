import sys

import telebot
from telebot import types


def main(token):
    bot = telebot.TeleBot(token)
    print("logged successfully")

    @bot.message_handler(commands=['start'])
    def on_hello(message):
        bot.send_message(message.from_user.id, "👋 Greetings! I am AaronR92's personal bot!")
        on_text_message(message)

    @bot.message_handler(content_types=['text'])
    def on_text_message(message):
        print(message.text)
        markup = types.InlineKeyboardMarkup()
        github = types.InlineKeyboardButton("💻 My GitHub", url="https://github.com/aaronr92")
        discord = types.InlineKeyboardButton("🦦 My Discord", url="https://discordapp.com/users/494204801761148928")
        telegram = types.InlineKeyboardButton("📱 My Telegram", url="https://t.me/aaronr92")
        vk = types.InlineKeyboardButton("📱 My VK", url="https://vk.com/antonr924")

        markup.add(github, discord, telegram, vk)
        bot.send_message(message.from_user.id, '🌐 Links to my social media', reply_markup=markup)

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main(sys.argv[1])
