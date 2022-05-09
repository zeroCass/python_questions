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
import threading
import requests
from bs4 import BeautifulSoup
from donwload_img import img_scrape
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def donwload_xkcd(inicio = None, fim = None) -> None:
    '''
        inicio e fim estao invertidos nessa funcao
        dessa forma, inicio > fim e isso eh garantido
        *ficou mt confuso dessa maneira, o site funciona assim tbm
    '''
    if inicio is not None and fim is not None and inicio < fim:
        [i, f] = [fim, inicio]
    else:
        [i, f] = [inicio, fim]
    
    
    if i is None:
        res = requests.get('https://xkcd.com/')
        page = BeautifulSoup(res.text, 'html.parser')
        i = page.find('a', {'rel': 'prev'})['href'].replace('/', '')
        i = int(i) + 1

    if f is None:
        f = 1


    thread_list = []
    increase = round((int(i) - int(f)) * 0.25)
    for x in range(int(f), int(i) + 1, increase):

        # verifica se xf (x_final) eh maior do que o fim 
        # se for, entao xf = fim
        xf = (x + increase) - 1
        if xf > int(i):
            xf = int(i)

        logging.debug(f'x: {x} - xf(fim): {xf}')

        # cria thread para cada funcao 
        th = threading.Thread(target=img_scrape, args=(str(x), str(xf)))
        thread_list.append(th)
        th.start()  # incia a thread
    
    # espera cada thread terminar
    for th in thread_list:
        th.join()
    logging.debug('Done.')



def main():
    t = time.perf_counter()

    if len(sys.argv) == 2:
        donwload_xkcd(sys.argv[1])
    elif len(sys.argv) >= 3:
        donwload_xkcd(sys.argv[1], sys.argv[2])
    else:
        donwload_xkcd()

    print(f'time passed: {time.perf_counter() - t}')

if __name__ == '__main__':
    main()