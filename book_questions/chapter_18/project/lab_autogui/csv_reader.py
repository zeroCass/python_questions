'''
Passado o nome de um arquivo csv
o programa ira verificar se o arquivo eh valido e segue o padrao determinado
se sim, retornara uma list de dict
'''

import csv
import os

csv_foler = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'csv_files')
print(csv_foler)

def csv2dict(file_name, pattern: list) -> list:
    l = []
    with open(file_name, newline='') as csvfile:
        reader = list(csv.reader(csvfile))

        if reader[0] != pattern:
            print('Pattern is not sattisfy')
            return None
        d = {}
        for row in reader:
            d[reader[0][0]] = row[0] 
            d[reader[0][1]] = row[1]
            l.append(d) 
        
    return l
