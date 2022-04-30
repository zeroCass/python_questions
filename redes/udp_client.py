from socket import *

server_name = 'localhost'
server_port = 9999
client_socket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase setence: ').encode()
# retorna o tamanho do dado que foi enviado
status = client_socket.sendto(message, (server_name, server_port))

# se houve dados enviados, entao espera alguma resposta do servidor
if status > 0:
    modified_message, server_adress = client_socket.recvfrom(2048)
    print(f'Message: {modified_message}\n Server Adress: {server_adress}')
client_socket.close()