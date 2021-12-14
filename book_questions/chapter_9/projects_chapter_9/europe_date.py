'''
Capitulo 9

Projeto: Renomeando arquivos com datas em estilo
americano para datas em estilo europeu


Suponha que seu chefe envie milhares de arquivos a você por email com datas
em estilo americano (MM-DD-AAAA) nos nomes dos arquivos e precise que
eles sejam renomeados com datas em estilo europeu (DD-MM-AAAA). Essa
tarefa maçante poderia exigir um dia inteiro para ser feita manualmente!
Vamos criar um programa para fazer isso.
Eis o que o programa deve fazer:
• Procurar todos os nomes de arquivo no diretório de trabalho atual em busca
de datas em estilo americano.
• Quando um arquivo for encontrado, ele deverá ser renomeado com o mês e
o dia trocados para deixar a data em estilo europeu.
Isso significa que o código deverá fazer o seguinte:
• Criar uma regex que possa identificar o padrão de texto para datas em estilo
americano.
• Chamar os.listdir() para encontrar todos os arquivos no diretório de trabalho.
• Percorrer todos os nomes de arquivo em um loop usando a regex para
verificar se ele contém uma data.
• Se houver uma data, o arquivo deverá ser renomeado com shutil.move().
Para esse projeto, abra uma nova janela no editor de arquivo e salve seu
código como renameDates.py.
'''


import os, re
import shutil

# muda o diretorio atual para o dir do current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

american_format = re.compile(r'''^(.*?)   # todo texto antes
    ((0|1)?\d)- # um ou dois dígitos para o mês
    ((0|1|2|3)?\d)- # um ou dois dígitos para o dia
    ((19|20)\d\d) # quatro dígitos para o ano
    (.*?)$''', re.VERBOSE)


#print(american_format.search('12-31-2000').group())


for root, sub_dir, files in os.walk(os.getcwd()):
    for file in files:
        #print(f'sub-folder: {sub_dir}')
        # cria objet match para a regex
        mo = american_format.search(file)
        # verifica se esse objeto eh valido
        if mo:
            # cria string que contem a data no novo formato usado os grupos da regex
            # grupo 1 - parte anterior a data
            # grupo 2 - dia
            # grupo 4 - mes
            # grupo 6 - ano
            # grupo 7 - parte posterior a data 
            europe_format = mo.group(1) + mo.group(4) + '-' + mo.group(2) + '-' + mo.group(6) + mo.group(8)
            print(europe_format)

            print(type(file))

            #file_dir = os.path.realpath(file)[:len(mo.group())]
            # print(file_dir)
            # american_filename = os.path.join(file_dir, file)
            # europe_filename = os.path.join(file_dir, europe_format)
            
            #shutil.move(os.path.join(os.getcwd(),file), os.path.join(os.getcwd()))