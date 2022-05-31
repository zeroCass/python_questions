"""
Problema:
João conseguiu contratar um ótimo plano de Internet para o seu telefone celular. O plano permite que João utilize uma quota de até 
X megabytes de dados por mês para navegar na Internet. Se João não usa toda a sua quota no mês, os megabytes que ele não usou são 
adicionados à quota do mês seguinte. Pelo contrato, João nunca pode usar mais megabytes do que a sua quota corrente. Por exemplo, 
se X=200 megabytes e João usou 150 no primeiro mês e 220 megabytes no segundo mês, então no terceiro mês João tem uma quota 
de 230 megabytes para usar (50 megabytes são transferidos do primeiro para o segundo mês, 30 megabytes são transferidos do segundo 
para o terceiro mês). Nesta tarefa são dados o valor da quota mensal X e quantos megabytes João usou em cada um dos primeiros N meses do plano. 
Você deve determinar quantos megabytes João tem para usar no mês N+1.

Entrada
A primeira linha da entrada contém um número inteiro X, o valor da quota mensal em megabytes.
 A segunda linha contém um inteiro N, o número de meses. Cada uma das linhas seguintes contém um número inteiro M_i, 
 indicando a quantidade de megabytes que João usou em cada mês, do mês 1 até o mês N.

Saída
Seu programa deve produzir uma única linha, contendo um único número inteiro, a quantidade de megabytes que João tem para usar no mês N+1.
"""

#logica:
# mb_total = quantidade de megabytes de dados por mes que Joao possui
# quota = quanitadade de megabytes nao utilizados, ou seja, um bonus que aumenta a qtd de megabytes disponiveis para uso.
# se Joao nao usa esso o mb_total, a quota nao utilizada eh somada ao mb_total para que ele tem mais megabytes no proximo mes

#entao o todo mes consideramos que há um acrescimo de megabytes na qtd total de megabytes (comecando em 0) disponivel:
#   mb_disponivel = mb_total + quota
#eh feito o calculo da sobra (quota) do proximo mes:
#   quota = mb_disponivel - qtd_utilizada


mb_total = int(input())
meses = int(input())
quota = 0

while meses > 0:
    mb_disponivel = mb_total + quota
    qtd_utilizada = int(input())
    quota = mb_disponivel - qtd_utilizada
    meses -= 1

#saida = quota disponivel para o mes que vem + qtd de megabytes totais do plano
print(quota + mb_total)