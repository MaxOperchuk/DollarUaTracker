import os

import telebot
from dotenv import load_dotenv

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
    bot.reply_to(message, "1 USD = 4.00 TRY")


bot.polling()
