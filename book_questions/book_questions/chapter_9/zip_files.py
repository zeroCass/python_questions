'''
Capitulo 9

Extraindo arquivos com modulo zipfile
'''

import zipfile, os

# current dir
dir = os.path.dirname(os.path.abspath(__file__))

file_zip = 'zip_test.zip'
# cria obejto zipfile para manipular esse arquivo zipado
example_zip = zipfile.ZipFile(os.path.join(dir, file_zip))

# retorna todos os arquvos/pastas contidos no zip
print(example_zip.namelist())

for item in example_zip.namelist():
    print(f'Tamanho do arquivo {item}: {example_zip.getinfo(item).file_size}\n'
            f'Tamanho comprimido: {example_zip.getinfo(item).compress_size}\n\n')

extract2folder = os.path.join(dir, 'extract_folder')
# extrair um arquivo para outra pasta que nao seja o dir atual
example_zip.extract('zip_test/zip_file_test.txt', extract2folder)

# extrai todos os arquivos para a pasta atual
os.chdir(dir)                   # muda o dir atual para o dir do arquivo python sendo executado
example_zip.extractall()

# fecha o file descriptor
example_zip.close()