from socket import *

host = '192.168.10.1'
port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

data = input('Input lowercase setence: ')

client_socket.sendall(str.encode(data))
data = client_socket.recv(1024)

print(f'Message: {data.decode()}')