import telebot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling()