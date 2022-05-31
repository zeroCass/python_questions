"""
Problema:

Um pangrama é uma frase que contém todas as letras de um determinado alfabeto.

Em português, um pangrama pode incluir também letras acentuadas, mas neste problema vamos desconsiderar os acentos 
(mesmo que isso torne a frase mal escrita!)

Veja alguns exemplos de pangramas em português (sem acentos):

grave e cabisbaixo, o filho justo zelava pela querida mae doente
hoje a noite, sem luz, decidi xeretar a quinta gaveta de vovo: achei linguica, pao e fuba
marta foi a cozinha pois queria ver belo jogo de xicaras
Note que para os pangramas acima consideramos o alfabeto composto pelas letras

a b c d e f g h i j l m n o p q r s t u v x z

(ou seja, não consideramos as letras k, w ou y). Note ainda que as frases não contêm letras acentuadas mas podem conter símbolos 
gráficos como espaço em branco, vírgula e dois pontos.

Entrada
A primeira e única linha da entrada contém uma cadeia de caracteres C.

Saída
Seu programa deve produzir uma única linha, contendo um único caractere, que deve ser S se a frase for um pangram ou N caso contrário.
Restrições
A cadeia de caracteres C tem no mínimo um e no máximo 200 caracteres. Os únicos caracteres em C são as letras minúsculas do alfabeto mostrado acima, espaços em branco, vírgulas e o caractere dois pontos.
"""


#logica:
# eh feito um loop que percorre todas as letras do alfabeto desconsiderando k,w e y
# entao eh feita uma verificacao se aquela determina letra esta presente na palavra fornceida usando a funcao find()
# se a letra nao esta presente, entao a variavel pangama = false e o loop retorna false

def pangrama (palavra: str) -> bool:
    letra = 97
    pangrama = True
    while pangrama and letra <= 122:
        if chr(letra) == 'k' or chr(letra) == 'w' or chr(letra) == 'y':
            letra += 1
            continue

        if palavra.find(chr(letra)) == -1:
            print(chr(letra))
            pangrama = False
        letra += 1
    return pangrama


palavra = input()
if pangrama(palavra):
    print('S')
else:
    print('N')