from http.client import CONFLICT, HTTPConnection
import json

conn = HTTPConnection('', 12000)
content = {'login': 'mariazinha', 'password': '12345'}
#conn.request('POST', '/adduser', json.dumps(content))

conn.request('GET', '/user', json.dumps({'id': 1}))

response = conn.getresponse()
data = response.read()
print(response)
print(data)
conn.close()