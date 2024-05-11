import os

import telebot
from dotenv import load_dotenv

from parser.xpath_parser import get_exchange_rate

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Hello, I am a bot. "
        "Enter the command /get_exchange_rate "
        "to get the USD to UAH exchange rate.")


@bot.message_handler(commands=["get_exchange_rate"])
def send_exchange_rate(message):
    exchange_rate = get_exchange_rate()
    bot.reply_to(message, exchange_rate)


bot.polling()
