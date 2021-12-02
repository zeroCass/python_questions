'''
Livro - Automatize Tarefas Macantes com Python by Al Sweigart
Capitulo 7

Projetos práticos:
Detecção de senhas robustas

Crie uma função que utilize expressões regulares para garantir que a string de
senha recebida seja robusta. Uma senha robusta deve ter pelo menos oito
caracteres, deve conter tanto letras maiúsculas quanto letras minúsculas e ter
pelo menos um dígito. Talvez seja necessário testar a string em relação a
diversos padrões de regex para validar sua robustez.
'''

import re
def is_strong_pwd (password: str) -> bool:
    ''' this function will check if some password is strong based on:
        1 - has at least 8 characters
        2 - has letters upper and lower case
        3  at least 1 digit
        4 - at lest 1 special character 
     '''

    # check if has at least 8 characters
    pwd = re.compile(r'^(\w{8,}')
    if not pwd.search(password):
        return False

    # has letters upper and lower case  
    upper = re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    if not upper.search(password) and lower.search(password):
        return False

    # at least 1 digit
    digit = re.compile(r'\d+')
    if not digit.search(password):
        return False
    
    special_char = re.compile(r'[/*-+.@&%#!,:/?^]')
    if not special_char.search(password):
        return False


    return True


pwd_input = input()
if is_strong_pwd(pwd_input):
    print('Password is strong!')
else:
    print('Password is weak')
