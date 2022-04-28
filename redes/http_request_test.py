import http.client
import requests


# estabelece conexao http, que faz comunicacao com host e a port
conn = http.client.HTTPConnection('www.python.org', 80)
# estabelece os parametros e o arquivo na qual o request ira fazer
conn.request('GET', '/')
# pega a reposta ao request
http_resp = conn.getresponse()


print(http_resp.getheaders())
html = http_resp.read()
print(html.decode())

conn.close()

res = requests.get('https://www.python.org')
print(res.text)