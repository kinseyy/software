from colorama import init, Fore, Back

bad_gateway = (Fore.RED + "BAD GATEWAY ---> 403 Forbidden " + Fore.WHITE + "[NOT OK]")
code_200 = (Fore.GREEN + "Successfully installed.\nStarting load " + Fore.WHITE + "[OK]")
dbg_pring = (Fore.CYAN + "[Debug]")
dbg_job_doing_error = (Fore.MAGENTA + "[RUN]" + Fore.RED + "")
dbg_pring_warnable = (Fore.YELLOW + "WARNING!")
dbg_pring_trouble = (Fore.RED + "GYP ERR!")
dbg_js_prefix = (Fore.MAGENTA + "HTTP:GET/nodejs")
rst = (Fore.RESET + " ")

class package_messages:
     def register_message_success():
          print(dbg_pring + rst + Back.GREEN + " Wrapping project")
     def register_message_failure():
          print(dbg_pring + rst + Back.RED + " Project compiled with error")
     def Forbidden(self, backage, sourcepeckt, usercache, loginas, saveentry, env, security_space):
          print("Not available now")
     def addenv(self, from_srv_data):
          print()