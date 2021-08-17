import telebot, re

TOKEN = re.sub("\\s", "", open("token.txt").readline())
bot = telebot.TeleBot(TOKEN)
print("Initialized.")
