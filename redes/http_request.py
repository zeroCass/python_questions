import http.client

HOST = 'localhost'
PORT = 12000


conn = http.client.HTTPConnection(HOST, PORT)
conn.request('GET', '/index.html')
res = conn.getresponse()
print(res.status, res.reason)
data = res.read().decode()
print(data)
conn.close()