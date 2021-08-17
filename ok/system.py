import re
from bot import bot
import messages, objects, gameplay


def log(message):
    name = message.chat.first_name + " " + message.chat.last_name
    nick = '@' + message.chat.username
    user = name + " (" + nick + ", ID: " + str(message.chat.id) + ")"
    print(user, ": \"", message.text, "\"", sep="")

@bot.message_handler(commands=['help'])
def help(message):
    log(message)
    bot.send_message(message.chat.id, messages.HELP)

@bot.message_handler(commands=['join'])
def help(message):
    log(message)
    gid = re.sub("/join\\s*", "", message.text)
    gameplay.join(message.chat.id, gid)

@bot.message_handler(commands=['create'])
def help(message):
    log(message)
    roles = re.sub("/create\\s*", "", message.text).split()
    gameplay.create(message.chat.id, roles)


def start_bot():
    bot.polling()
#    bot.infinity_polling()
