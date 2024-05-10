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


