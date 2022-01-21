import config
import telebot

bot = telebot.TeleBot(config.api_key, parse_mode=None)


@bot.message_handler(commands=['oy'])
def oy(message):
    bot.send_message(message.chat.id, 'Welcome to the Lazed Bot mga KaBred. Here are some helpful commands \n /updates for our latest release \n /socials for our social media pages \n /poops for pooping activity')


@bot.message_handler(commands=['updates'])
def updates(message):
    bot.send_message(
        message.chat.id, 'Mayroon kaming bagong single! Stream Mabuting Balita now on Spotify: https://open.spotify.com/track/1Rnha1QQciUNy1d0BeZrSH?si=0e05477a07a1412d')


@bot.message_handler(commands=['socials'])
def socials(message):
    bot.send_message(
        message.chat.id, '@lazednapt everywhere')


@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(
        message.chat.id, 'new message')


@bot.message_handler(commands=['poops'])
def test(message):
    bot.send_message(
        message.chat.id, 'Thomas Alva Edison')


bot.polling(allowed_updates=[])
