# hi, hyd? - Ker

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docopt import docopt
from googlesearch import search
from colorama import Fore
import os
import requests

class info:
    __version__ = "{}[*] {}NoD0rk v1.0 {}SHIO".format(Fore.RED,Fore.WHITE,Fore.MAGENTA)
    red = Fore.RED
    green = Fore.GREEN
    white = Fore.WHITE
    yellow = Fore.YELLOW
    cyan = Fore.CYAN
    banner = r"""{}      

 __   __     ______     _____     ______     ______     __  __    
/\ "-.\ \   /\  __ \   /\  __-.  /\  __ \   /\  == \   /\ \/ /    
\ \ \-.  \  \ \ \/\ \  \ \ \/\ \ \ \ \/\ \  \ \  __<   \ \  _"-.  
 \ \_\\"\_\  \ \_____\  \ \____-  \ \_____\  \ \_\ \_\  \ \_\ \_\ 
  \/_/ \/_/   \/_____/   \/____/   \/_____/   \/_/ /_/   \/_/\/_/ 

                                                             v1.0

                                                    
    """.format(Fore.RED)

usg = """{}NoD0rk, A simple, easy to use Dorker
{}
Usage:
    nodork1.py <args> <page> [options]
    nodork1.py (-h | --help)

Args:
    <url>    URL parameter that will be dorked.
    <page>   Amount of page

Options:
    -h, --help    Show this screen
    -s            Automatically Saves the file as "DorkedLinks.txt"


""".format(info.cyan,info.white)

def FileSave(link):
    with open ("DorkedLinks.txt", "a") as f:
        f.write(link + "\n")
        f.close()

def DeleteFile():
    try:
        if os.path.exists:
            os.remove("DorkedLinks.txt")
        else:
            print("{}[x] {}There's nothing to delete!".format(info.red,info.white))
    except:
        print("{}[x] {}There's nothing to delete!".format(info.red,info.white))

def clearTerminal():
    os.system("cls" or "clear")

def searchWeb():
    clearTerminal()
    print(info.banner)
    print(info.__version__)
    print("{}".format(info.white))
    os.system("title NoD0rk")


    args1 = docopt(usg)
    params = args1['<args>']
    resNum = args1['<page>']

    try:
        count = 0

        # Checking connection
        print("{}[*] {}Checking the connection...".format(info.cyan,info.white))
        req_result = requests.get("https://ident.me/")
        if req_result.status_code != 200:
            print("{}[x] {}Cannot connect to the internet.".format(info.red,info.white))
            exit()
        else:
            print("{}[!] {}Connection Established.".format(info.cyan,info.white))
        
        # fetches the result
        for a in search("inurl:" + params, num_results=int(resNum)):
                result = print(f"{info.green}[!] {info.white}Link Found! {info.cyan}{a}")
                link = a
                FileSave(link)
                count = count + 1

        print(f"{info.green}[+] {info.white}Links Scraped: {info.green}{count}{info.white}")
        if args1["-s"]:
            exit()
        else:
            pass
        ans = input("{}[!] {}Do you want to keep the file? (y/n) ".format(info.yellow,info.white))
        ans.lower()
        if ans == "y":
            pass
        elif ans == "n":
            DeleteFile()
        else:
            print("Please choose. (y/n)")
                
    except Exception as e:
        print(f"{info.red}[x] {info.white}Something wrong occurred. {info.red}{e}")
        print(f"{info.green}[+] {info.white}Links Scraped: {info.green}{count}{info.white}")
        if args1["-s"]:
            exit()
        
        elif count == 0:
            exit()

        else:
            pass
        ans = input("{}[!] {}Do you want to keep the file? (y/n) ".format(info.yellow,info.white))
        ans.lower()
        if ans == "y":
            pass
        elif ans == "n":
            DeleteFile()
        else:
            print("{}[!] {}Please choose. (y/n)".format(info.yellow,info.white))
        

def initialize():
    print(f"{info.yellow}[+] {info.white}{info.__version__}")
    searchWeb()


if __name__ == "__main__":
    initialize()
