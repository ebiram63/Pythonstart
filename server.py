import socket

from base64 import encode




bind_ip = "127.0.0.1"
bind_port = 9999

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((bind_ip, bind_port))
serv.listen()

print("Server is Running.....")

clt,addr = serv.accept()
print("new connection %s"%str(addr))
clt.send("Hello I am at your service".encode())
serv.close()
