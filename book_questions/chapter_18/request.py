import requests
import bs4

res = requests.get('http://10.233.87.11:631')
html = bs4.BeautifulSoup(res.text, 'html.parser')
print(html)