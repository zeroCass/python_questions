'''
Capitulo 9

Projeto: Fazer backup de uma pasta usando um arquivo ZIP

Suponha que você esteja trabalhando em um projeto cujos arquivos são
mantidos em uma pasta chamada C:\AlsPythonBook. Você está preocupado
em perder seu trabalho, portanto gostaria de criar arquivos ZIP que sejam
“snapshots” (imagens instantâneas) de toda a pasta. Você gostaria de manter
diferentes versões, portanto quer que o nome dos arquivos ZIP seja
incrementado a cada vez que for criado; por exemplo, AlsPythonBook_1.zip,
AlsPythonBook_2.zip, AlsPythonBook_3.zip e assim por diante. Isso poderia
ser feito manualmente, porém é uma tarefa irritante e você poderia
acidentalmente usar um número incorreto nos nomes dos arquivos ZIP. Será
muito mais simples executar um programa que realize essa tarefa maçante
para você.
Para esse projeto, abra uma nova janela no editor de arquivo e salve o
programa como backupToZip.py.
'''

import os, sys
import zipfile

def backup_to_zip(folder):
    try:
        if not os.path.isabs(folder):
            raise Exception('Invalid path folder')
    except Exception as inst:
        print(inst)
    
    os.chdir(os.path.dirname(os.path.abspath(folder)))

    number = 1
    zip_filename = ''
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    print('zipfile that will be created: %s' % (zip_filename))
    zip = zipfile.ZipFile(zip_filename, 'w')

    # percorre a pasta (basename) inteira e adiciona cada arquivo//diretorio no zip
    for root, sub_dir, files in os.walk(os.path.basename(folder)):
        print('adding files in %s' % root)
        # acresceta pasta atual no arquivo zip
        zip.write(root)

        for file in files:
            # nao faz backup de arquivos .zip
            if not str(file).endswith('.zip'):
                # escreve o arquivo passando seu path (raiz e o arquivo)
                zip.write(os.path.join(root, file))
    zip.close()



def main():
    if len(sys.argv) <= 1:
        folder = r'C:\Users\05694223101\Documents\python\python issues\book_questions\chapter_9'
    else:
        # pega o caminho passado em arg
        # o join serve para os casos em que ha algum whitespace no path
        folder = ' '.join(sys.argv[1:])

    backup_to_zip(folder)

if __name__ == '__main__':
    main()