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

# muda o diretorio atual para o dir do current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

europe_format = re.compile(r'''(
    ((0{1}[1-9]{1})|(1{1}[0-2]{1}) )
    (\s|-|\.)+
    (\d{2})
    (\s|-|\.)+
    (\d{4})
    )''', re.VERBOSE)

# emails = re.compile(r'''(
#         ([a-zA-Z0-9._%+-]+)             # nome de usuario
#         @                               # simbolo @ obrigatorio
#         ([a-zA-Z0-9._%+-]+)             # dominio
#         (\.[a-zA-Z]{2,5})               # ponto seguindo por mais caracteres
#         ((\.[a-zA-Z]{2,5}))?
#         ((\.[a-zA-Z]{2,5}))?
#     )''', re.VERBOSE)

print(europe_format.findall('10-15-2000'))

# for root, sub_dir, files in os.walk(os.getcwd()):
#     for file in files:
#         print(europe_format.search(file).group())