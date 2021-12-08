import os


# muda para o diretorio do arquivo atual
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# pega o diretorio anterior (chapter_8)
chapter_8 = (os.path.join(os.path.abspath('..'), 'chapter_8'))


for folder, subfolders, files in os.walk(chapter_8):
    print(f'current folder:{folder}')
    for subfolder in subfolders:
        print(f'subfolder of {folder}: {subfolder}')
        for file in subfolder:
            print(f'file {file} inside {subfolder}')
    for file in files:
        print(f'file {file} inside {folder}')
    print()