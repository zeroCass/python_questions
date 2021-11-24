import sys, os


# get the dir path of current pathname module
dir_base = os.path.dirname(os.path.abspath(__file__))

# retorna o path da concatenacao do path + obj path
file_dir = os.path.join(dir_base, 'files')

# pega o file
file_name = 'wiki.txt'
file = os.path.join(dir_base, file_dir, file_name)


try:
    with open(file) as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)

