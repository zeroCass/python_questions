'''
Handler: Manipulador de pedidos
É um processo de tratamento de chamadas, ou seja
O handler recebe um request e processa de acordo com um padrao:
    Nesse caso, um http handler processando metodos get, put... e inserindo cabeçalhos necesarios
'''


import http.server
import socketserver

HOST = 'localhost'
PORT = 12000
httpd = None

try:
    # cria um handler http para processador requests do tipo get, put..
    handler = http.server.SimpleHTTPRequestHandler
    # cria um socket, do tipo handler
    httpd = socketserver.TCPServer((HOST, PORT), handler)
    # metodo que fica atendendo ao requests
    httpd.serve_forever()
except Exception as e:
    if httpd is not None:
        # encerra os pedidos
        httpd.shutdown()
        # encarra o socket 
        httpd.server_close()
