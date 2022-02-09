from socket import *


host = 'localhost'
port = 12000



server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print('Server is Current Runnning...\n Waiting for connection')
conn, addr = server_socket.accept()
data = None
while not data:
    data = conn.recv(1024)
    conn.sendall(data.upper())

print('Closing connection')
conn.close()


