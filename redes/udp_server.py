from http import server
from  socket import *

server_host = 'localhost'
server_port = 9999

# cria o socket
# AF_INET -> especifica que a familia do endereco esta usando IPV4
# SOCK_DGRAM -> indifica que socket sera do tipo UDP
server_socket = socket(AF_INET, SOCK_DGRAM)

# atribui o host e a porta para o objeto socket 
server_socket.bind((server_host, server_port))
print('Server is running')

while True:
    message, client_adress = server_socket.recvfrom(2048)
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_adress)


