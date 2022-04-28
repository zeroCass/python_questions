"""
Problema:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


# logica:
# deve existir 2 loops, 1 para cada inteiro
# dessa forma, podemos variar o inteiro j diversas vezes ate chegar no maior numero possivel que possui 3 algorismos (999)
# entao dentro do segundo loop, iremos multiplcar por exemplo 100 * j, onde j irá possuir todos os valores possiveis entre 100 e 999
# sempre que houve algum palindromo, este sera armazenado em uma variavel apenas se o palindromo atual for maior que o anterior


palindrome = 100                    # comeca em 100 pois precisamos de um numero de 3 digitos
for i in range(1000):
    j = i

    for j in range(1000):
        pal = str(i * j)            # multiplica dois inteiros para ver se o rsultado eh palindromo
        pal_reverse = pal[::-1]     # reverte o resultado e armazena em uma variavel
        
        if pal == pal_reverse:      # verifica se de fato eh palindromo
            pal = int(pal)          # converte para inteiro
            if pal > palindrome:    # so troca se o palindromo calculado for maior que o palindromo atual (armazenado)
                palindrome = pal


print(palindrome)


# a = 'abc'
# b = a[::-1]                       # (slice notation) step igual a -1 ou seja, esta indo de tras para frente
# print(b)