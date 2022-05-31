import requests

content = {'login': 'mariazinha', 'password': '12345'}
#res = requests.post('http://localhost:12000/usuarios', data=content)
res = requests.get('http://localhost:12000/usuarios/lista', params={'id': '1'})