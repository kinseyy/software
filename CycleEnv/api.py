import os
import sys
import time
import platform
import colorama
from colorama import init, Fore
import urllib.request

dbg_pring = (Fore.CYAN + "[Debug]")
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
        print(dbg_pring + rst + "")
        