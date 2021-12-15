'''
Capitulo 9

Apagando arquivos desnecessários

Não é incomum que algumas pastas ou alguns arquivos enormes e
desnecessários ocupem a maior parte do espaço de seu disco rígido. Se você
estiver tentando disponibilizar espaço em seu computador, será muito mais
vantajoso apagar os maiores arquivos indesejados. Porém será preciso
localizá-los antes.
Crie um programa que percorra uma árvore de diretórios e procure arquivos
ou pastas que sejam excepcionalmente grandes – por exemplo, aqueles que
tenham um tamanho de arquivo maior que 100 MB. (Lembre-se de que, para
obter o tamanho de um arquivo, os.path.getsize() do módulo os poderá ser
utilizado.) Mostre esses arquivos na tela com seus paths absolutos.
'''

import os, sys
def useless_files(folder):
    ''' mostra ao usuario arquivos maiores que 100KB dada um dir 
        obs: o valor original foi alterado para KB para nao pesar nada
    '''
    target_size = 100000

    try:
        if not os.path.isabs(folder):
            raise Exception('Invalid path folder')
    except Exception as inst:
        print(inst)

    for root, sub_dir, files in os.walk(folder):
        for file in files:
            # verifica arquivos em que o tamanho eh maior que target_size
            if os.path.getsize(os.path.join(root, file)) > target_size:
                print(f'folder: {os.path.basename(root)}')
                print(f'____file: {file}    size: {os.path.getsize(os.path.join(root, file))}')
                print(f'absolute path: {os.path.abspath(os.path.join(root, file))}')



def main():
    if len(sys.argv) <= 1:
        folder = r'C:\Users\05694223101\Documents\python\python issues\book_questions\chapter_9'
    else:
        # pega o caminho passado em arg
        # o join serve para os casos em que ha algum whitespace no path
        folder = ' '.join(sys.argv[1:])

    useless_files(folder)

if __name__ == '__main__':
    main()