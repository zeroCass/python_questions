import http.client
import requests

HOST = 'localhost'
PORT = 12000


conn = http.client.HTTPConnection(HOST, PORT)
conn.request('GET', '/index.html')
res = conn.getresponse()
print(res.status, res.reason)
data = res.read().decode()
print(data)
conn.close()


res = requests.get('http://localhost:12000/index.html')
print(res.text)