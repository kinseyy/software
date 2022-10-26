import paramiko
import platform

from colorama import init, Fore, Back
init()

def checksys():
     if platform.system() == "Windows":
          print(Fore.GREEN + "Windows is supported")
     else:
          print(Fore.RED + platform.system() + " not supported")
checksys()

def cluster():
     input("~ ")

def recovery(admin_hostname, admin_username, admin_password, user_for_recovery):
     user_inputbox = str(input("New passphrase for recovery: "))

     client = paramiko.client.SSHClient()
     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     client.connect(admin_hostname, username=admin_username, password=admin_password)
     stdin, stdout, stderr = client.exec_command('passwd ' + user_for_recovery)
     stdin.write(user_inputbox + '\n')
     stdin.write(user_inputbox + '\n')
     stdin.flush()

     stdout.channel.set_combine_stderr(True)
     print(stdout.read().decode())
     client.close()

def runcmd():
     exec = input("Run command")
     client = paramiko.client.SSHClient()
     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     client.connect(admin_hostname, username=admin_username, password=admin_password)
     stdin, stdout, stderr = client.exec_command(exec)
     stdin.write(user_inputbox + '\n')
     stdin.write(user_inputbox + '\n')
     stdin.flush()

     stdout.channel.set_combine_stderr(True)
     print(stdout.read().decode())
     client.close()