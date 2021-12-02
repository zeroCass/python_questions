'''
Livro - Automatize Tarefas Macantes com Python by Al Sweigart
Capitulo 6

Projeto: Adicionando marcadores na marcação da
Wiki

O script bulletPointAdder.py obterá o texto do clipboard, adicionará um
asterisco e um espaço no início de cada linha e, em seguida, colará esse novo
texto no clipboard.
'''

import sys, pyperclip

text = pyperclip.paste()
lines = text.split('\n')


for idx in range(len(lines)):
    lines[idx] = '* '  + lines[idx]

text = '\n'.join(lines)
pyperclip.copy(text)
