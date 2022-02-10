import http.server
import socket
import socketserver

HOST = 'localhost'
PORT = 12000
httpd = None

try:
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), handler)
    httpd.serve_forever()
except Exception as e:
    if httpd is not None:
        httpd.shutdown()
        httpd.server_close()
        