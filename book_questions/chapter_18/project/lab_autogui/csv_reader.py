'''
Passado o nome de um arquivo csv
o programa ira verificar se o arquivo eh valido e segue o padrao determinado
se sim, retornara um dict
'''

import csv

def csv2dict(file_name):
    d = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        if reader.line_num == 1:
            # adicionar chaves de acordo o primeiro valor de cada coluna
            # ex: 3 colunas -> nome, id, valor (3 chaves, nome, id e valor)
            # adicionar lista com valores para cada chave(coluna)
            pass
    