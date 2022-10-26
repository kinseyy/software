import paramiko

hostname = 'vmi.phylex.space'
port = 22
username = 'noroot_vmi95'
password = 'nrv95'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    s.close()