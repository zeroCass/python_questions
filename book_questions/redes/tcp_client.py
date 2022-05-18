'''
Funcoes para monitorar tempo foram implementadas de forma didática

Da mesma forma que o server ira blocar o codigo em quanto espera para receber dados,
o client também.

'''

from socket import *
import time

host = 'localhost'
port = 12000

# instncia o socket e define o tipo de conexçao e o tipo de dado que sera recebido/transmitodo
client_socket = socket(AF_INET, SOCK_STREAM)
# conecta o socket com um endereco em uma porta passada por parametro
client_socket.connect((host, port))

data = input('Input lowercase setence: ')

# envia dados para a conexao estabelecida
client_socket.sendall(str.encode(data))


while True:
    # recebe dados da conexao socket
    last_time = time.time()
    data = client_socket.recv(1024)
    if not data:
        break
    time_passed = time.time() - last_time
    print(f'Message: {data.decode()}\nTime passed to recieve data: {time_passed}')

client_socket.close()
