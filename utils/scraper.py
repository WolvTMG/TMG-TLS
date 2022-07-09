import json
import time
import discord
import threading
from os.path import exists
from discord.ext import commands

from plugins import common


configfile = 'config.json'

def inputtoken():
    token = input(f"Input Token: ")

    data = {
        "token": token
    }

    with open(configfile, 'w') as file_object:
        json.dump(data, file_object)

    return data


if not exists(configfile):
    data = inputtoken()
else:
    with open('config.json', 'r') as f:
        data = json.load(f)

token = data["token"]


def scrape():
    
    common.clear()
    common.logo()

    def returns():

        e = input("Type exit to return\n\nType #userlist to scrape friends ID's\n\n").lower()
        if e == 'exit':
            print("Ok")

    process = threading.Thread(target=returns)
    process.start()

    bot = commands.Bot(command_prefix='#', self_bot=True)

    @bot.command()
    async def userlist(ctx):
        await ctx.message.delete()
        data = []
        for user in bot.user.friends:
            data.append(user.id)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=1)

    try:
        bot.run(token, bot=False)
    except discord.LoginFailure:
        print('Invalid Token')
        time.sleep(2.5)
        common.clear()

def conf():

    common.logo()

    token = input("Type exit to return\n\nPress enter to confirm ")
    if token == 'exit':
        print("Alright")
        time.sleep(1)
    else:
        scrape()
