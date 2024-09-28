import telebot
import sqlite3
from config import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)

class Calories:
    pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'PLACEHOLDER')


@bot.message_handler(commands=['help'])
def send_commands_list(message):
    bot.reply_to(message, 'COMMANDS LIST')


@bot.message_handler(commands=['count_calories'])
def calorie(message):
    pass


bot.infinity_polling()