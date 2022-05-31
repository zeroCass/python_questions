from http.client import CONFLICT, HTTPConnection
import json

conn = HTTPConnection('', 12000)
content = {'login': 'mariazinha', 'password': '12345'}
#conn.request('POST', '/usuarios', json.dumps(content))

conn.request('GET', '/usuarios/lista')

response = conn.getresponse()
data = response.read()
print(response)
print(data)
conn.close()