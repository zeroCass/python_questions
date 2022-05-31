'''
Livro - Automatize Tarefas Macantes com Python by Al Sweigart
Capitulo 7

Projetos práticos:

Versão de strip() usando regex
Crie uma função que receba uma string e faça o mesmo que o método de
string strip(). Se nenhum outro argumento for passado além da string em que
a remoção será feita, os caracteres de espaço em branco serão removidos do
início e do fim da string. Caso contrário, os caracteres especificados no
segundo argumento da função serão removidos da string.
'''
import re

def strip_regex (string,to_strip=None):
    if to_strip == None:
        to_strip = '^(\s+)|(\s+)$'
    return re.sub(to_strip, '', string)


print(strip_regex(' ola mundo '))
print(strip_regex(' ola mundo ', 'o'))