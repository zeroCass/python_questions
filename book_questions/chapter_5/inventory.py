'''
Livro - Automatize Tarefas Macantes com Python by Al Sweigart
Capitulo 5

Projeto Pratico - Função de “lista para dicionário” para o inventário de jogo de
fantasia

Suponha que os despojos de um dragão vencido seja representado como uma
lista de strings como esta:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Crie uma função chamada addToInventory(inventory, addedItems), em que
o parâmetro inventory seja um dicionário representando o inventário do
jogador (como no projeto anterior) e o parâmetro addedItems seja uma lista
como dragonLoot. A função addToInventory() deve retornar um dicionário
que represente o inventário atualizado.
'''


# python - automatizando coisas livro
# exercicios de dicionario

def display_inventory (inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(v, k)
        total_items += v
    print('Total number of items: {}'.format(total_items))


dic = {'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, \
    'dagger':1}


def add_to_inventory (inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
        

dic = {'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, \
    'dagger':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


display_inventory(inv)
add_to_inventory(inv, dragonLoot)
display_inventory(inv)