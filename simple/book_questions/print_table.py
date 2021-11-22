'''
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

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


table_format = ''
for i in range(len(tableData)):
    col_width = [0] * len(tableData)
    print(col_width)
    for j in range(len(tableData[i])):
        table_format += tableData[i][j].rjust(col_width)

print(table_format)