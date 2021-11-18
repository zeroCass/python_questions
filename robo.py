"""
Problema:
Um fazendeiro comprou um robô-espantalho para espantar os pássaros de sua plantação de milho. O robô se move ao longo de um caminho que circunda a plantação.
 No caminho há N estações numeradas sequencialmente, a partir de 1, no sentido horário. A figura abaixo mostra um exemplo com oito estações.


O robô inicia cada dia na estação número 1, e então obedece a uma sequência de comandos. Os comandos são gerados por um algoritmo de aprendizagem de máquina 
que coleta informações através de sensores espalhados na plantação, para garantir uma cobertura de vigia máxima. Cada comando faz com que o robô se mova para outra estação, 
vizinha à estação em que ele se encontra, ou no sentido horário ou no sentido anti-horário. O robô permanece nessa nova estação até receber um novo comando.

Apesar da promessa de que o robô protegeria a plantação, ao final de um determinado dia o fazendeiro notou que parte de sua plantação estava devastada por pássaros.
 O fazendeiro agora quer entender melhor o que aconteceu.

Dados o número da estação mais próxima à área devastada e a sequência de comandos que o robô obedeceu naquele dia, escreva um programa para determinar 
quantas vezes o robô permaneceu na estação mais próxima à àrea devastada.


Entrada
A primeira linha contém três inteiros N, C e S, representando respectivamente o número de estações, o número de comandos e o número da estação mais próxima à área devastada. A segunda linha contém C inteiros X1, X2, …, XC, representando a sequência de comandos recebidos pelo robô. Para i = 1, 2, …, C, se Xi é 1 então o i-ésimo comando significa "mova-se para a próxima estação no sentido horário", enquanto se Xi é -1 então o i-ésimo comando significa "mova-se para a próxima estação no sentido anti-horário". O robô sempre inicia na estação número 1.

Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, o número de vezes que o robô permaneceu na estação número S durante o dia.
"""

# logica:
# armazenar os comandos dados ao robo em uma lista
# percorrer essa lista e para cada comando (item), somar a estacao_atual pelo valor do comando (1/-1)
# sendo assim, o robo sempre andará ou pra frente ou para tras, de acordo com o sentido horario.
#
# para garantir isso, tem que ser feito uma comparacao para que o valor da estacao_atual nunca extrapole os limites:
#   se a estacao_atual (que sempre comeca em 1 e o comeco eh sempre 1) for menor do que 1, entao o valor dela passa ser o ultimo valor
#   se a estacao_atual for maior do que o maior valor possivel, entao ela reseta e volta para posicao 1
# com isso, criamos um ''circulo'', onde o robo sempre anda em circulo na direcao horaria
#
# depois eh so feita uma simples comparacao para saber se a estacao_atual do robo eh a estacao que o client quer que ele esteja e armazena quantas vezes ele
# passou por lá em uma variavel


comandos_totais = []
num_estacoes, num_comandos, estacao_target = input().split()    # entrada de dados
comandos_totais = input().split()                               # armazena dados na lista de comadnos


num_estacoes = int(num_estacoes)                                # conversao de dados para inteiro
num_comandos = int(num_comandos)
estacao_target = int(estacao_target)

estacao_atual = 1                                              # sempre comeca na primeira estacao
contador = 0                                                   # conta qtd de vezes q o robo permaneceu na estacao target durante o dia

# eh necessario verificar se ele ja esta na estacao targe caso a estacao seja igual a 1
if estacao_atual == estacao_target:
        contador += 1

for comando in comandos_totais:

    comando = int(comando)
    estacao_atual += comando

    if estacao_atual < 1:
        estacao_atual = num_estacoes

    if estacao_atual > num_estacoes:
        estacao_atual = 1

    if estacao_atual == estacao_target:
        contador += 1

print(contador)
    
