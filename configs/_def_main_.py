from pyrogram import Client, filters
from ryas_templates.chattext import *
from ryas_templates.botones import *
from pyrogram import *
from datetime import datetime
import os, requests, re, time
from configs.configsBot import *
from _mainConten_ import *

def ryas(bit):
    nix = Client.on_message(filters.command(bit, ["/", ".", ",", "-", "$", "%"]))
    return nix

def ryasbt(bor):
    nox = Client.on_callback_query(filters.regex(bor))
    return nox

def conta(call):
    if call == 'apid':
        return apid
    elif call == 'hasd':
        return apihasd
    else:
        return token 

usertime = {}
timetake = 30

def atspam(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if 5416957433 in usertime and time.time() - usertime[user_id] < timetake:
            await func(client, message)
            usertime[user_id] = time.time()
            return
        elif user_id in usertime and time.time() - usertime[user_id] < timetake:
            wait_time = int(timetake - (time.time() - usertime[user_id]))
            await message.reply(f"<b>[•] Contro de spam await <code>{wait_time} sg.</code> </b>")
            return
        else:
            await func(client, message)
            usertime[user_id] = time.time()

    return wrapper

# Added print statement
print('Bienvenido a ryas onn')
