import os
import sys
import time
import threading

from plugins import themes

def clear():
    system = os.name
    if system == 'nt':
        #if its windows
        os.system('cls')
    elif system == 'posix':
        #if its linux
        os.system('clear')
    else:
        print('\n'*120)
    return 

def SlowPrint(_str):
    for letter in _str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

def tls():
    global themes

    print(themes.theme + """
                         ████████╗███╗   ███╗ ██████╗               ████████╗██╗     ███████╗
                         ╚══██╔══╝████╗ ████║██╔════╝               ╚══██╔══╝██║     ██╔════╝
                            ██║   ██╔████╔██║██║  ███╗    █████╗       ██║   ██║     ███████╗
                            ██║   ██║╚██╔╝██║██║   ██║    ╚════╝       ██║   ██║     ╚════██║
                            ██║   ██║ ╚═╝ ██║╚██████╔╝                 ██║   ███████╗███████║
                            ╚═╝   ╚═╝     ╚═╝ ╚═════╝                  ╚═╝   ╚══════╝╚══════╝
                                                                    
                                            

                    [1] Token Checker   | [2] Spammer        | [3] Discord Server | [4] Webhook Checker
                    [5] Nuker           | [6] Scrape Friends | [7] Scrape Invites | [8] Log into an acc
                    [9] Coming soon     | [10] Coming soon   | [11] Coming soon   | [12] Coming soon
                    [13] Coming soon    | [14] Coming soon   | [15] Coming soon   | [16] Coming soon
                    [17] Coming soon    | [18] Coming soon   | [19] Themes        | [20] Exit


""")


def the():
    print("""
                              ████████╗██╗  ██╗███████╗███╗   ███╗███████╗███████╗
                              ╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝██╔════╝
                                 ██║   ███████║█████╗  ██╔████╔██║█████╗  ███████╗
                                 ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║
                                 ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗███████║
                                 ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝

                                [1] Original     | [2] Blue         | [3] Yellow
                                [4] White        | [5] Black        | [6] Exit


""")

def logo():
    print("""         
                         ████████╗███╗   ███╗ ██████╗               ████████╗██╗     ███████╗
                         ╚══██╔══╝████╗ ████║██╔════╝               ╚══██╔══╝██║     ██╔════╝
                            ██║   ██╔████╔██║██║  ███╗    █████╗       ██║   ██║     ███████╗
                            ██║   ██║╚██╔╝██║██║   ██║    ╚════╝       ██║   ██║     ╚════██║
                            ██║   ██║ ╚═╝ ██║╚██████╔╝                 ██║   ███████╗███████║
                            ╚═╝   ╚═╝     ╚═╝ ╚═════╝                  ╚═╝   ╚══════╝╚══════╝

""")
