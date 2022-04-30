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

server_socket.timeout(5)

while True:
    message, client_adress = server_socket.recvfrom(2048)
    # o valor null deve ser enviado pelo client manualmente, o protocolo UDP nao garante que a conexao seja finalizada sozinha
    # entao eh importante configurar timeout
    if not message:
        break
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_adress)
server_socket.close()
