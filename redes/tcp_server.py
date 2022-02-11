'''
Funcoes para monitorar tempo foram implementadas de forma didática

A funcao accept do modulo socket, ira travar o codigo, pois ira ficar 
esperando que uma conexao seja para continuar a execucao do codigo.
O mesmo vale para receber dados. Em quanto não receber dados, o codigo ficara esperando.

Dessa forma, é valida a criação de threads para cada conexão feita ao servidor. Acho que
esse seria o conectio de handler client.
'''


from socket import *
import time

host = 'localhost'
port = 12000

# instacia o socket do server, informado o time de conexcao e o tipo de dados que serao transmitidos/recebidos
server_socket = socket(AF_INET, SOCK_STREAM)
# atribui para o socket um host e uma porta, para que ele seja um server
# ''diz ao SO que uma certa porta esta associada ao socket
server_socket.bind((host, port))


# permite que o socket server fique escutando qualquer request que venha de outro processo
print('Server is Current Runnning...\n Waiting for connection')
server_socket.listen()

last_time = time.time()
# aceita um request de conexcao
conn, addr = server_socket.accept()
print(f'Coneccation accedpted. Time passed: {time.time() - last_time}')


data = None
while True:
    last_time = time.time()
    data = conn.recv(1024)
    print(f'Timed passed to recivie data: {time.time() - last_time}')
    if not data:
        break
    time.sleep(5)
    conn.sendall(data.upper())

print('Closing connection')
conn.close()


