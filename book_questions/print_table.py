'''
Livro - Automatize Tarefas Macantes com Python by Al Sweigart
Capitulo 6

Projeto Pratico - Exibicao de tabela

Crie uma função chamada printTable() que receba uma lista de listas de
strings e a exiba em uma tabela bem organizada, com cada coluna justificada
à direita. Suponha que todas as listas internas contenham o mesmo número de
strings. Por exemplo, o valor poderá ter o seguinte aspecto:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

Sua função printTable() exibirá o seguinte:
    apples Alice dogs
    oranges Bob cats
    cherries Carol moose
    banana David goose
'''

import sys

def print_table(table):
    # como sugerido no livro, col_width eh um array inicializado em 0 que indica o tamanho da maior palavra
    # em cada coluna. Com base no exeplo dado, iremos considerar a tabela de dimensao x,y como sendo y,x
    # ou seja, se antes era 3x4, agora sera 4x3, contando 3 colunas
    col_width = [0] * len(table)

    # este for serve para percorrer a tabela de maneira a respeitar a inversao comentada acima
    # entao para cada coluna da tabela, sera verificado qual a maior palavra e entao sera armazenado em col_with
    for y in range(len(table)):
        for x in range(len(table[0])):
            if len(table[y][x]) > col_width[y]:
                col_width[y] = len(table[y][x])

    # de fato agora a tabela sera printada e justificada a direita com base no tamanho 
    # da maior palavra da coluna
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(col_width[y]), end=' ')
        print() 





table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)