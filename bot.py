import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['oy'])
def start(message):
    bot.reply_To(message, 'Oy! Kumusta! Welcome to the Lazed Bot')


bot.polling()
