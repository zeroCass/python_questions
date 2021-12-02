'''
Este eh uma versao alternativa do arquivo strong_password.py
usando a tecnica do lookahead da regex
a expressao do lookahead eh: ?=

Nesse caso, ?=.*[A-Z] ira considerar:
    procure à frente qualquer caracteres de zero ou mais ocorrencias do grupo A-Z
'''

import re
def is_strong_pwd (password: str) -> bool:
    ''' this function will check if some password is strong based on:
        1 - has at least 8 characters
        2 - has letters upper and lower case
        3  at least 1 digit
        4 - at lest 1 special character 
     '''

    #pwd = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
    pwd = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#?!@$%^&*-.]).{8,}$')
    if not pwd.search(password):
        return False
    return True


pwd_input = input()
if is_strong_pwd(pwd_input):
    print('Password is strong!')
else:
    print('Password is weak')