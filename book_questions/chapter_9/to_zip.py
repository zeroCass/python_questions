'''
Capitulo 9

Zipando um arquivo
OBS:com o metodo write, ele zipa somente um arquvio, entao para zipar mais de um
eh necssario usar dentro do os.walk() por exemplo 

Alternativa para zipar varios arquivos:
shutil.make_archive()
'''


import zipfile, os

# muda diretorio atual
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# cria um arquivo zip
file_to_zip = 'to_zip'
new_zip = zipfile.ZipFile(f'{file_to_zip}.zip', 'w')

# escreve osarquivos no zip, passando o tipo de comprensao
new_zip.write(file_to_zip, compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()