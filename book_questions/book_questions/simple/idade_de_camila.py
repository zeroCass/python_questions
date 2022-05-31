"""
Problema:
Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador...
 Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos.
Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos que Cibele nasceu antes de Camila e 
Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.

Entrada
A entrada é composta por três linhas, cada linha contendo um número inteiro N, a idade de uma das irmãs.

Saída
Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila. 
"""


# logica:
# a idade de camila eh sempre a do meio, entao o programa recebe 3 entradas (idades das irmas)
# que sao armazenadas em um array
# esse array eh ordenado e como ja dito, a idade de camila eh sempre a do meio (array[1])
idades = []
for i in range(3):
    idades.append(int(input()))

idades.sort()
print(idades[1])




