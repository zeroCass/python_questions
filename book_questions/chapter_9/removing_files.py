import os, shutil ,send2trash


dir = os.path.dirname(os.path.abspath(__file__))

# unlink deleta permanentemente um arquivo
file2delete = os.path.join(dir, 'mad_libs.txt')
if os.path.exists(file2delete):
    os.unlink(file2delete)
    print(f'O arquivo {file2delete} foi excluido')

# os.rmdir -> remove uma pasta vazia

# shutil.rmtree -> remove a pasta e todos os arquivos dentro
dir2delete = os.path.join(dir, 'provas_backup')
if os.path.exists(dir2delete):
    shutil.rmtree(dir2delete)
    print(f'A pasta {dir2delete} foi deleteada')

file2trash = os.path.join(dir, 'mad_copy.txt')
if os.path.exists(file2trash):
    send2trash.send2trash(file2trash)
    print(f'Arquivo/Pasta foi movido para a lixeira')



