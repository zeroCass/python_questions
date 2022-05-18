'''
Capitulo 11

Projeto: Downloading de todas as tirinhas XKCD

Os blogs e outros sites atualizados regularmente em geral têm uma página
inicial com a postagem mais recente, além de um botão Previous (Anterior)
na página que conduzirá você à postagem anterior. Então essa postagem
também terá um botão Previous e assim sucessivamente, criando um percurso
que conduz da página mais recente até a primeira postagem do site. Se quiser
uma cópia do conteúdo do site para ler quando não estiver online, você
poderá navegar manualmente por todas as páginas e salvar cada uma delas.
Contudo esse é um trabalho bem maçante, portanto vamos criar um programa
que faça isso.
'''


import requests
from bs4 import BeautifulSoup
import os
import sys
import logging
import time


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)



def img_downloader(url:str) -> BeautifulSoup:
    '''
        faz o donwload de uma pagina dado seu url
        faz o scrape da img dentro da pagina e faz seu download
        salva a img baixado no diretorio 'xkcd'
    '''

    # faz download da pagina
    print(f'\nDonwloading page {url}')
    res = requests.get(url)
    res.raise_for_status()
    # pega o conteudo html da pagina
    page = BeautifulSoup(res.text, 'html.parser')

    img_src = page.find('div', id='comic').img['src']
    print(f'Download image {os.path.basename(img_src)}')
    img = requests.get('http:' + img_src)

    with open(os.path.join('xkcd', os.path.basename(img_src)), 'wb') as img_file:
        for chunk in img.iter_content(100000):
            img_file.write(chunk)
    
    # autaliza a url com base na url anterior
    prev = page.find('a', {'rel': 'prev'})['href']
    if prev != '#':
        prev = prev.replace('/', '')
    return 'https://xkcd.com/' + prev



def img_scrape(inicio:str = None, fim:str = None) -> None:
    '''
    '''

    if inicio is not None and fim is not None and int(inicio) < int(fim):
        [inicio, fim] = [fim, inicio]

    url = 'https://xkcd.com/'
    if inicio is not None:
        url += str(inicio)

    if fim is None:
        fim = '#'
    
    logging.debug(f'fim: {fim} - inicio: {inicio}\n')

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs('xkcd', exist_ok=True)
    
    url_fim = url.split('/')[-1]
    while not fim == url_fim:
        url_fim = url.split('/')[-1]
        url = img_downloader(url)
            

def main():
    t = time.perf_counter()

    if len(sys.argv) == 2:
        img_scrape(sys.argv[1])
    elif len(sys.argv) >= 3:
        img_scrape(sys.argv[1], sys.argv[2])
    else:
        img_scrape()

    print(f'time passed: {time.perf_counter() - t}')


if __name__ == '__main__':
    main()


