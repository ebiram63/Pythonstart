import socket

cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cli.connect(("127.0.0.1" , 9999))

cli.send("GET / HTTP/1.1\r\nHost:127.0.0.1:9999\r\n\r\n".encode())

res = cli.recv(4096)

print(res)