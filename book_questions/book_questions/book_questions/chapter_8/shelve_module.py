'''
O modulo shelve permite salvar variaveis em arquivos,
para que possa ser importado depois durante o programa
'''

import shelve, os, sys
dir = os.path.dirname(os.path.abspath(__file__))

shelf_file = shelve.open(os.path.join(dir, 'mydata'))
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats

#print(list(shelf_file.keys()))
shelf_file.close()