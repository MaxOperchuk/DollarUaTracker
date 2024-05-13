import os

import telebot
from dotenv import load_dotenv

from database.extract_data import fetch_data
from writer.xlsx_writer import write_to_xlsx


load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Hello, I am a bot. "
        "Enter the command /get_exchange_rate "
        "to get the USD to UAH exchange rate.",
    )


@bot.message_handler(commands=["get_exchange_rate"])
def send_exchange_rate(message):
    data = fetch_data()
    write_to_xlsx(data)

    with open("exchange_rates.xlsx", "rb") as file:
        bot.send_document(message.chat.id, file)

    os.remove("exchange_rates.xlsx")


bot.polling()
