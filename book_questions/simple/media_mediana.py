"""
A média de três números inteiros A, B e C é (A + B + C)/3. 
A mediana de três números inteiros é o número que ficaria no meio se os três números fossem ordenados em ordem não-decrescente.

Sua tarefa é escrever um programa que, dados dois números inteiros distintos A e B,
 calcule o menor inteiro possível C tal que a média e a mediana de A, B e C sejam iguais.

Entrada
A entrada é composta de uma única linha contendo dois números inteiros A e B.

Saída
Seu programa deve produzir uma única linha, contendo um único número, o menor inteiro possível C tal que a média e
 a mediana de A, B e C são iguais.
"""
#logica:
#precisa-se encontrar um valor X que seja a media de 3 numero e que tbm seja a mediana
#logo, a formula para achar a icognita:
#   (X + A + B)/3 = A   #onde A é a media e a media
# X = (A * 3) - A - B

a, b = input().split()
a = int(a)
b = int(b)
x = 3 * a - a - b
print(x)