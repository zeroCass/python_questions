'''
Capitulo 9

Copiando/Movendo arquivos usando modulo:
shutil
'''

import shutil, os, sys

# change diretory
os.chdir('c:\\')
# get current working directory
print(os.getcwd())

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

# go to the previos path and get in chapter_8 folder
chapter_8 = (os.path.join(os.path.abspath('..'), 'chapter_8'))
#print(chapter_8)
#sys.exit()

# shitil.copy -> copia UM arquivo dado um path para outro path
file_name = 'mad_libs.txt'
shutil.copy(os.path.join(chapter_8, file_name), os.getcwd())
# obs: se o arquiivo existir, ira sobrescreber

# copytree -> copia todos os arquivos e subpastas dentro de um diretorio para outra pasta (cria essa pasta)
file_name = 'provas_files'
try:
    shutil.copytree(os.path.join(chapter_8, file_name), os.path.join(os.getcwd(), 'provas_backup'))
except FileExistsError:
    print('Arquivo já existe')


# move -> move/renomeia um arquivo de um lugar para outro
#  shuti.move(origi, destino)
file_name = 'mad_libs.txt'
if not os.path.exists(os.path.join(os.getcwd(), 'mad_copy.txt')):
    shutil.move(os.path.join(chapter_8, file_name), os.path.join(os.getcwd(), 'mad_copy.txt'))

# OBS: se o destino for uma pasta, o arquivo sera movido.
#           caso o destina contenha um arquivo com o msm nome, este será sobrescrito
#           se no destino conter um nome de arquivo, este será movido e renomeado 