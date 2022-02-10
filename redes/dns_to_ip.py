import time
import socket

# pega o nome do host -> string (seria algo tipo dns)
nome = socket.gethostname()
print(nome)
# pega o IP a partir do dns (hostname)
ip = socket.gethostbyname(nome)
print(ip)
# pega o dns (hostname) a partir do IP adress
print(socket.gethostbyaddr(ip))
