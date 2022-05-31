import requests
import bs4

res = requests.post('http://10.233.87.11:631/printers/CBHRBZRECEP', data={'administration':'modify-printer'})
html = bs4.BeautifulSoup(res.text, 'html.parser')
print(html.prettify())