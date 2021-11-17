"""
Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um nível de jogo, que é representado por um número inteiro: 
quanto maior o número, melhor o nível do jogador.

Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o jogo mais interessante, eles querem que os níveis 
dos dois times formados sejam o mais próximo possível. O nível de um time é a soma dos níveis dos jogadores do time.

Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons em algumas outras coisas, como lógica ou matemática. 
Você pode ajudá-los e encontrar a menor diferença possível entre os níveis dos times que podem ser formados?

Entrada
A entrada contém quatro linhas, cada linha contendo um inteiro A, B, C e D, indicando o nível de jogo dos quatro amigos.

Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, a menor diferença entre os níveis dos dois times formados.
"""

#logica:
#colocar as entradas em um array
#ordenar esse array
#com o array ordenado, temos o primeiro numero sendo o menor e o maior numero sendo o ultimo, logo:
#   para manter os times equilibrados, o menor numero precisa obrigatatoriamente ficar com o maior numero
#   entao o time 1 eh a soma do menor numero mais o menor numero
#   o time 2 eh a soma dos valores restante
#a diferencao eh entao calculada subtraindo a soma do time 1 - soma do time 2

a = int(input())
b = int(input())
c = int(input())
d = int(input())

array = [a, b, c, d]
array.sort()

time0 = array[0] + array[3]
time1 = array[1] + array[2]
print(abs(time0 - time1))       # valor absoluta para que nao haja valores negativos