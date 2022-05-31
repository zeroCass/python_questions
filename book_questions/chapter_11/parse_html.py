import requests, bs4
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# faz o donwload do conteudo da pagina web
res = requests.get('https://nostarch.com/')
# gera erro caso a requesiscao nao tenha exito
res.raise_for_status()
# cria o obj BeautifulSoup passando uma string contendo html
no_starch_soup = bs4.BeautifulSoup(res.text, 'html.parser')
with open(os.path.join(os.getcwd(),'parse_html.html')) as file:
    # cria um obj BeautifulSoup passando um arquivo contendo html
    file_soup = bs4.BeautifulSoup(file.read(), 'html.parser')

# metodo select(), retorna uma lista contendo todas as tags de um seletor CSS informado pra funcao
elems = file_soup.select('#author')
print(elems)
for elements in elems:
    print(elements)
# pega somente o texto contido na tag
print(elems[0].getText())
# informa o id e o seu nome
print(elems[0].attrs)

# metodo get rtorna valore de atributos de um elemento
id = file_soup.select('span')[0].get('id')
print(id)






