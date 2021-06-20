#!/usr/bin/python3
import config 
import telegram
import os
import subprocess
import sys
import shlex
import datetime
from subprocess import Popen, PIPE
from telegram.ext import CommandHandler
from imp import reload 

from telegram.ext import Updater
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

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


def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Text One')
    updater.dispatcher.add_handler(CommandHandler('start', start))

def id(update, context):
    userid = update.message.from_user.id
    context.bot.sendMessage(chat_id=update.message.chat_id, text=userid)

def help(update, context):
    reload(config)
    context.bot.sendMessage(chat_id=update.message.chat_id, text='''список доступных команд:
    /id - id пользователя
    /curlsh - узнать ip telegram бота
    /powersh - имитировать нажатие кнопки питания ~0.5c
    /longpowersh - имитировать долгое нажатие кнопки питания ~8c
    /pingsh - проверить доступность сервера через ping
    ''')


#функция команады curlsh
def curlsh(update, context):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("curl.sh")
        context.bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

def powersh(update, context):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("power.py")
        context.bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

def pingsh(update, context):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("ping.sh")
        context.bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

def longpowersh(update, context):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("longpower.py")
        context.bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

curlsh_handler = CommandHandler('curlsh', curlsh)
dispatcher.add_handler(curlsh_handler)

curlsh_handler = CommandHandler('powersh', powersh)
dispatcher.add_handler(curlsh_handler)

curlsh_handler = CommandHandler('longpowersh', longpowersh)
dispatcher.add_handler(curlsh_handler)


curlsh_handler = CommandHandler('pingsh', pingsh)
dispatcher.add_handler(curlsh_handler)


myid_handler = CommandHandler('id', id)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
