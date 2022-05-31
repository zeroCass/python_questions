
'''
Capitulo 12

Projeto: Ler dados de uma planilha

Suponha que você tenha uma planilha com dados do censo norte-americano
de 2010 e tenha a tarefa maçante de verificar seus milhares de linhas para
contabilizar a população total e o número de setores censitários de cada
condado. (Um setor censitário é simplesmente uma área geográfica definida
para o censo.) Cada linha representa um único setor censitário. Chamaremos o
arquivo com a planilha de censuspopdata.xlsx e ele poderá ser baixado de
http://nostarch.com/automatestuff/.
'''
import os
import openpyxl


raiz = os.path.join(os.path.abspath('.'), 'automate_online-materials') 
wb = openpyxl.load_workbook(os.path.join(raiz, 'censuspopdata.xlsx'))
sheet = wb.active

county_data = {}

for row in range(2, 10):
    # cada linha contem dados de 1 setor 
    state = sheet[f'B{row}'].value
    county = sheet[f'C{row}'].value
    pop = sheet[f'D{row}'].value

    # garante que existe uma chave chamada state
    county_data.setdefault(state, {})
    # garante que exisite uma chave chamada county dentro de state, e que denrto de county exista um dicionario
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    # adiciona os valores nos respectivos campos [state][county]
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += pop
