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