import os
import sys
import time
import httpx
import discord
import requests
import colorama

from plugins import common
from plugins import themes

from utils import nuker
from utils import scraper
from utils import invites


colorama.init()

def main():

    common.SlowPrint("Booting TMG TLS\n")
    time.sleep(1.0)
    common.SlowPrint("Made by WolvTMG")
    time.sleep(1.0)
    common.clear()

    def tools():

        common.tls()

        select = input(f"                                                      Choice: ")
        if select == '1':
            common.clear()
            tools()
        elif select == '2':
            common.clear()
            tools()
        elif select == '3':
            common.clear()
            common.logo()
            e = input(".gg/uYCeDP3\n\n[Enter] to return")
            common.clear()
            tools()
        elif select == '4':
            common.clear()
            tools()
        elif select == '5':
            common.clear()
            nuker.conf()
            common.clear()
            tools()
        elif select == '6':
            common.clear()
            scraper.conf()
            common.clear()
            tools()
        elif select == '7':
            common.clear()
            invites.conf()
            common.clear()
            tools()
        elif select == '8':
            common.clear()
            tools()
        elif select == '9':
            common.clear()
            tools()
        elif select == '10':
            common.clear()
            tools()
        elif select == '11':
            common.clear()
            tools()
        elif select == '12':
            common.clear()
            tools()
        elif select == '13':
            common.clear()
            tools()
        elif select == '14':
            common.clear()
            tools()
        elif select == '15':
            common.clear()
            tools()
        elif select == '16':
            common.clear()
            tools()
        elif select == '17':
            common.clear()
            tools()
        elif select == '18':
            common.clear()
            tools()
        elif select == '19':
            common.clear()
            themes.themeChecker()
            tools()
        elif select == '20':
            sys.exit()
        else:
            common.clear()
            tools()

    tools()
main()