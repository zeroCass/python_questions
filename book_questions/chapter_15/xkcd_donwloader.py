''''
Capítulo 15
Projeto: Programa multithreaded para download de
XKCD

No capítulo 11, criamos um programa que fazia o download de todas as
tirinhas do site XKCD. Esse programa era single-threaded: ele baixava uma
tirinha de cada vez. A maior parte do tempo de execução do programa era
consumida para estabelecer a conexão com a rede, iniciar o download e
gravar as imagens baixadas no disco rígido. Se você tiver uma conexão de
banda larga com a Internet, seu programa single-threaded não estará
utilizando toda a largura de banda disponível.

Um programa multithreaded que tenha algumas threads baixando tirinhas
enquanto outras estão estabelecendo conexões e gravando os arquivos com as
imagens das tirinhas em disco usará sua conexão de Internet de maneira muito
mais eficiente e baixará a coleção de tirinhas mais rapidamente. Abra uma
nova janela no editor de arquivo e salve esse arquivo como
multidownloadXkcd.py. Você modificará esse programa para adicionar
multithreading. O código-fonte com as alterações completas está disponível
para download em http://nostarch.com/automatestuff/.
'''

import imp
import sys
import requests
from bs4 import BeautifulSoup
from donwload_img import img_scrape
#from ..chapter_11.projects_chapter_11.donwload_img import img_scrape


def donwload_xkcd(inicio = None, fim = None) -> None:
    i, f = None
    if inicio != None and fim != None and inicio < fim:
        [i, f] = [fim, inicio]
    else:
        [i, f] = [inicio, fim]
    
    
    if inicio is None:
        res = requests.get('https://xkcd.com/')
        page = BeautifulSoup(res.text, 'html.parser')
        i = page.find('a', {'rel': 'prev'})['href'].replace('/', '')
        i = int(i) + 1

    if fim is None:
        f = 1

    thread_list = []
    for x in range(int(i), int(f)):
        pass



def main():
    if len(sys.argv) == 2:
        donwload_xkcd(sys.argv[1])
    elif len(sys.argv) >= 3:
        donwload_xkcd(sys.argv[1], sys.argv[2])
    else:
        donwload_xkcd()


if __name__ == '__main__':
    main()