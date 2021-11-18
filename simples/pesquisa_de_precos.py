"""
Problema:
Uma jornalista está fazendo uma pesquisa de preços de combustíveis (álcool e gasolina), em vários estados do país, 
para uma reportagem sobre qual dos dois combustíveis é mais vantajoso para abastecer um carro.

Na reportagem ela vai usar a regra de que a utilização do álcool é vantajosa quando o preço por litro do álcool é no máximo igual a 70% do preço 
por litro da gasolina.

Ela compilou os dados da pesquisa em uma lista contendo o identificador do estado e os preços do litro de álcool e do litro de gasolina, 
e deseja computar em quais estados é mais vantajoso usar álcool ou gasolina. Você pode ajudá-la?

Entrada
A primeira linha da entrada contém um número inteiro N, o número de estados em que a pesquisa foi realizada. 
Cada uma das N linhas seguintes contém o identificador do estado, E, seguido de dois números reais A e G, representando respectivamente o 
preço do litro de álcool e o preço do litro de gasolina.

Saída
Para cada estado em que o álcool é vantajoso seu programa deve produzir uma linha, contendo somente o identificador do estado, 
na ordem em que os estados aparecem na entrada. Se em nenhum estado o álcool é vantajoso, seu programa deve imprimir uma linha contendo somente o caratere '*' (asterisco).
"""

# logica:
# em um loop, receber os inputs referentes ao estado e o valor do alcool/gasolina correspondente
# x = 70% do valor da gasolina, entao deve-se verificar se o valor do alcool eh no maximo igual a x
# se sim, entao adiciona 


estados = []
n = int(input())                # qtd de iteracoes do loop

while n > 0:
    estado, alcool, gasolina = input().split()
    alcool = float(alcool)
    gasolina = float(gasolina)

    x = gasolina * 0.7          # 70% do valor da gasolin
    
    if alcool <= x:             # se alcool for menor ou igual a 70% do valor da gasolina, entao esta ok
        estados.append(estado)  # adiciona estado no array de estados
    n -=1                       # decrementa para continuar loop

if len(estados) > 0:
    for estado in estados:
        print(estado)
else:
    print('*')
