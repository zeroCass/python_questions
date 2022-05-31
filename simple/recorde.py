"""
Problema:
Atletas conseguem resultados cada vez melhores! O recorde mundial de uma determinada modalidade esportiva é o melhor resultado conseguido por um atleta nessa modalidade,
 em competições oficiais. Competições oficiais incluem campeonatos mundiais, como os campeonatos mundiais de ginástica, atletismo ou natação, e também as Olimpíadas.

Como as Olimpíadas acontecem a cada quatro anos e competições oficiais acontecem todos os anos, é possível que o melhor resultado obtido em Olimpíadas em 
uma dada modalidade seja um resultado pior do que o recorde mundial para aquela modalidade. Por isso, nas provas das Olimpíadas são sempre mencionados dois recordes: 
o recorde olímpico (melhor resultado que já foi obtido em Olimpíadas) e o recorde mundial (melhor resultado em qualquer competição oficial, incluindo as Olimpíadas).

Nesta tarefa, dados o resultado de uma prova nas Olimpíadas e os recordes mundial e olímpico para essa prova, sua tarefa é determinar se o resultado é 
um novo recorde mundial e/ou um novo recorde olímpico.


Entrada
A entrada é composta por três linhas. A primeira linha é um inteiro R, o melhor resultado obtido por um atleta numa prova das Olimpíadas. 
A segunda linha é um inteiro M, o recorde mundial para essa prova. A terceira linha é um inteiro L, o recorde olímpico para essa prova. Para as provas desta tarefa, 
quanto menor o valor melhor o resultado.

Saída
Seu programa deve produzir duas linhas. A primeira linha deve ser RM se o resultado é um recorde mundial, ou * (asterisco) caso contrário.
 A segunda linha deve ser RO se o resultado é um recorde olímpico, ou * (asterisco) caso contrário.
"""


# logica:
# a solucao eh feita apenas com dois simples statements if/else
# eh importante notas que deve haver duas condicionais distantas pois o novo record pode ser tanto mundial quanto olimpico


melhor_result = int(input())
record_m = int(input())
record_o = int(input())

if melhor_result < record_m:
    print('RM')
else:
    print('*')

if melhor_result < record_o:
    print('RO')
else:
    print('*')
