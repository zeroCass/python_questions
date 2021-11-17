"""
Problema:
Uma palavra A é um anagrama de outra palavra B se podemos transformar a palavra A na palavra B apenas trocando de posição as letras da palavra A. 
Por exemplo, "iracema" é um anagrama de "america", e "estudo" é um anagrama de "duetos".

Podemos estender o conceito de anagramas para frases, desconsiderando caracteres que não são letras e apenas separam as palavras da frase. 
Assim, por exemplo, "porta coral" é um anagrama de "claro trapo". Também não é necessário que a palavra exista em alguma língua: 
"aca aaa bb b" é um anagrama de "ba.ba,aab ac".

Dadas duas frases, escreva um programa para determinar se elas são anagramas.

Entrada
A primeira linha da entrada contém um inteiro N, indicando o número de letras e espaços das frases. As duas linhas seguintes contêm respectivamente a frase A e a frase B, cada linha contendo exatamente N caracteres, entre letras, espaços em branco, vírgulas e pontos.

Saída
Seu programa deve produzir uma única linha, contendo um único caractere, que deve ser S se a frase for um anagrama ou N caso contrário.
"""


#logica:
# 1- criar uma funcao para contar a qtd de letras presentes em uma palavra
# 2-criar uma funcao para analisar duas strings e determinar se sao anagramas
#   - nessa funcao existira um loop que ira percorrer char por char de duas strings
#   - eh feita a chamada da funcao para contar a qtd de letras presentes na palavra para cada palavra
#   - se a qtd de letras de uma mesma letra presente nas duas palavras forem iguais, entao continua o loop, se nao sai
#   - se percorrer a palavra inteira e variavel ''iguais'' nao for alterada, entao as palavras sao anagramas


# conta quantas letras existem em uma palavra
def cont_letra (string: str, letra: str) -> int:
    qtd_letras = 0
    for l in string:
        if l == letra:
            qtd_letras += 1
    return qtd_letras


# retorna se duas strings sao anagramas
def anagrama (string_a: str, string_b: str) -> bool:
    iguais = True   # flag que mantem o loop rodando em quanto as palavras tiverem a msm quantiade de uma mesma letra
    letra_atual = 0 # indice da letra

    #  loop que percorre as strings
    while iguais and letra_atual < len(string_a):

        letra = string_a[letra_atual]   # letra = letra do indice atual

        # verifica se o char eh de fato uma letra, desconsidera caracteres especiais
        if ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122:
            qtd_letras_a = cont_letra(string_a, letra)
            qtd_letras_b = cont_letra(string_b, letra)

            # condicao de parada do loop
            if qtd_letras_a != qtd_letras_b:
                iguais = False
            
        letra_atual += 1    # icrementa o idx da letra atual


    return iguais


n = input()
a = input()
b = input()


if (anagrama(a,b)):
   print('S')
else:
   print('N')



