import paramiko
from getpass import getpass
host = ""

username = input("Enter Username :")
password = input("Enter Password :")

clt = paramiko.SSHClient(host, username, password)

clt.set_missing_host_key_policy(paramiko.AutoAddPolicy)

clt.connect(host, username=username, password=password)

stdin, stdout, stderr = clt.exec_command("ssh")

print(stdout.read(). decode())

