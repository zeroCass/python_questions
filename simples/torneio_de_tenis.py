"""
A prefeitura contratou um novo professor para ensinar as crianças do bairro a jogar tênis na quadra de tênis do parque municipal. 
O professor convidou todas as crianças do bairro interessadas em aprender a jogar tênis. Ao final do primeiro mês de aulas e treinamentos 
foi organizado um torneio em que cada participante disputou exatamente seis jogos. O professor vai usar o desempenho no torneio para separar 
as crianças em três grupos, de forma a ter grupos de treino em que os participantes tenham habilidades mais ou menos iguais, usando o seguinte 
critério:

participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;
participantes que não venceram nenhum jogo não serão convidados a continuar com os treinamentos.
Dada uma lista com o resultado dos jogos de um participante, escreva um programa para determinar em qual grupo ele será colocado.

Entrada
A entrada consiste de seis linhas, cada linha indicando o resultado de um jogo do participante. Cada linha contém um único caractere: 
V se o participante venceu o jogo, ou P se o jogador perdeu o jogo. Não há empates nos jogos.

Saída
Seu programa deve produzir uma única linha na saída, contendo um único inteiro, identificando o grupo em que o participante será colocado. 
Se o participante não for colocado em nenhum dos três grupos seu programa deve imprimir o valor -1.
"""

#logica:
#dentro de um loop sera informado uma string V (venceu) ou P (perdeu)
#entao existira uma variaveis para contar o numero de vitorias
#ao final do programa, a saida sera avaliada de acordo com a quantidade de vitorias do jogador

qtd_jogos = 6       # sempre serao 6 jogos avalidos
qtd_vitorias = 0    # variavel para guardar a quantidade de vitorias do jogador

while qtd_jogos > 0:
    resultado = input()
    if resultado == 'v' or resultado == 'V':
        qtd_vitorias += 1

    qtd_jogos -= 1

if qtd_vitorias >= 5:
    print(1)
elif qtd_vitorias >= 3:
    print(2)
elif qtd_vitorias >= 1:
    print(3)
else:
    print(-1)
