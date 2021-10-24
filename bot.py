#!/usr/bin/python3
import telebot
from telebot import types
import config
import subprocess
import sys
import shlex
import os
from imp import reload

bot = telebot.TeleBot(token=config.token)

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    global textoutput
    textoutput = ''
    while True:
        global output
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
        textoutput = textoutput + '\n' + output.strip()
    rc = process.poll()
    return rc

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello! This is a bot installed on rasspberry Pi to remotely turn on a home server. Enter /help for help.")

@bot.message_handler(commands=['help'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('/powersh')
	btn2 = types.KeyboardButton('/curlsh')
	btn3 = types.KeyboardButton('/pingsh')
	btn4 = types.KeyboardButton('/id')
	btn5 = types.KeyboardButton('/longpowersh')
	markup.add(btn1, btn2, btn3, btn4, btn5)
	send_mess = f"<b>Hello {message.from_user.first_name} {message.from_user.last_name}</b>!\nFor convenience, you can use the button.  \
        \n/id - id user\
        \n/curlsh - ip telegram bot server\
        \n/powersh - key power to push\
        \n/longpowersh - key power to push ~5s\
        \n/pingsh - local server status"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['curlsh'])
def start_command(message):
    reload(config)
    user = str(message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("curl.sh")
        bot.send_message(message.chat.id, text=textoutput)

@bot.message_handler(commands=['pingsh'])
def start_command(message):
    reload(config)
    user = str(message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("ping.sh")
        bot.send_message(message.chat.id, text=textoutput)

@bot.message_handler(commands=['powersh'])
def start_command(message):
    reload(config)
    user = str(message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("power.sh")
        bot.send_message(message.chat.id, text=textoutput)

@bot.message_handler(commands=['longpowersh'])
def start_command(message):
    reload(config)
    user = str(message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("longpower.sh")
        bot.send_message(message.chat.id, text=textoutput)

@bot.message_handler(commands=['id'])
def start_command(message):
    userid = message.from_user.id
    bot.send_message(message.chat.id, text=userid)

bot.polling()
