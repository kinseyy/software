import os
import sys
import time
import platform
import colorama
from colorama import init, Fore
import urllib.request

dbg_pring = (Fore.CYAN + "[Debug]")
dbg_pring_warnable = (Fore.YELLOW + "WARNING!")
dbg_pring_trouble = (Fore.RED + "GYP ERR!")
dbg_js_prefix = (Fore.MAGENTA + "HTTP:GET/nodejs")
rst = (Fore.RESET + " ")

class usercache:
    ip = urllib.request.urlopen ('http://ident.me').read().decode('utf8')

def sleeper(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

def startup():
    if platform.system() == "Windows":
        print(dbg_pring + rst + "Windows OS is supported!")
    else:
        print(dbg_pring_warnable + " " + dbg_js_prefix + rst + "OS not supported.")
        sleep(5)
        exit()
        


        