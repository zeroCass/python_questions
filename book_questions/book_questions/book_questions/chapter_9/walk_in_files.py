'''
Capitulo 9

Percorrendo um diretorios e suas subpastas/arquivos
os.walk()
'''

import os

# muda para o diretorio do arquivo atual
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# pega o diretorio anterior (chapter_8)
chapter_8 = (os.path.join(os.path.abspath('..'), 'chapter_8'))


for root, subdir, files in os.walk(chapter_8):
    print(
        f'root: {root}\n'
        f'sub-dir: {subdir}\n'
        f'files: {files}\n\n'
    )