import time
import json
import discord
import threading
from os.path import exists
from discord.ext import commands

from plugins import common


def scrape():

    e = input("Deee")

    bot = commands.Bot(command_prefix='#', self_bot=True)

    @bot.command()
    async def serverinvites(ctx):
        server = bot.get_server("server_id")
        link = bot.create_invite(destination=server, xkcd=True, max_age=0, max_uses=0)
        await ctx.send(link)

def conf():

    common.logo()

    token = input("Type exit to return\n\nPress enter to confirm ")
    if token == 'exit':
        print("Alright")
        time.sleep(1)
    else:
        scrape()
