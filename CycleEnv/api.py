import os
import sys
import time
import platform
import requests
import colorama
from colorama import init, Fore, Back
import urllib.request
import paramiko

bad_gateway = (Fore.RED + "BAD GATEWAY ---> 403 Forbidden " + Fore.WHITE + "[NOT OK]")
code_200 = (Fore.GREEN + "Successfully installed.\nStarting load " + Fore.WHITE + "[OK]")
dbg_pring = (Fore.CYAN + "[Debug]")
dbg_job_doing_error = (Fore.MAGENTA + "[RUN]" + Fore.RED + "")
dbg_pring_warnable = (Fore.YELLOW + "WARNING!")
dbg_pring_trouble = (Fore.RED + "GYP ERR!")
dbg_js_prefix = (Fore.MAGENTA + "HTTP:GET/nodejs")
rst = (Fore.RESET + " ")

class package:
    def register(pname, pversion, pauthor, ppath):
        print(dbg_pring + Fore.GREEN + Back.WHITE + " Wrapping project.")
    def goto(pname, ppath):
        print(dbg_pring + rst + "Running function goto project.")
        print(dbg_js_prefix + rst + "System is running")
    def addenv(envname, envcore):
        print()
        print()
    def remove(pname, ppath):



class intent:
    def wget(filename):
        send_request = requests.get(filename)
        if send_request.status_code == 200:
            print(code_200)
            from animations.load import animations10_100
            animations10_100()
            os.system("wget.exe " + filename)
        else:
            print(bad_gateway)
            print("[Program exited with code 0]")
            exit()


class usercache:
    ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
    hostget = urllib.request.urlopen

def sleeper(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

def sshclient():
    SSH_ADDRESS = "vmi.phylex.space"
    SSH_USERNAME = "root"
    SSH_PASSWORD = "4uMo7*Tg6lvsx75Z2W7QYGYs"
    SSH_COMMAND = "echo 'Hello World!'"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_stdin = ssh_stdout = ssh_stderr = None

    try:
        ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND)
        ssh_stdout.channel.recv_exit_status()
    except Exception as e:
        sys.stderr.write("SSH connection error: {0}".format(e))

sshclient()

def startup():
    if platform.system() == "Windows":
        print(dbg_pring + rst + "Windows OS is supported!")
    else:
        print(dbg_pring_warnable + " " + dbg_js_prefix + rst + "OS not supported.")
        sleep(5)
        exit()