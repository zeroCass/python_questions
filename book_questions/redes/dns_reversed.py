import socket

L = int(input())
while L > 0:
    ip = input()
    print(socket.gethostbyaddr(ip)[0])
    L -= 1