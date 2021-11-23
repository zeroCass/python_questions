# modulo da regex (expressoes regulares)
import re 


# criar um obj regex usando re.compile() -> o parametro fornecido corresponde ao padrao que o obj regex terá
phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')       # o r'' indica uma raw string (string pura, permitindo caracteres como ',", \, etc)

# o obj regex tem um metodo search(que recebe a string que vc quer pesquiar)
# esse metodo retornara um obj match
mo = phone_number_regex.search('My number phone is 415-555-4242')

# obj match tem um metodo group que ira retornar a string com o texto pesquisado caso encontre
print(f'Phone number found: {mo.group()}')
print()

####################################
# adicionar paratenses separa o obj regex em grupos
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phone_number_regex.search('My number phone is 415-555-4242')
print(f'Group 1: {mo.group(1)}')
print(f'Group 2: {mo.group(2)}')
print(f'All Groups: {mo.group()}')
print()



# adicionar caractres scapados por \
phone_number_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search('My number phone is (415)-555-4242')
print(f'Number with (): {mo.group()}')
print()



# correspondencia de varios grupos com pipe (|)
# eh possivel fazer uma regex conter um grupo na qual ira retornar o primeiro grupo achado quando pesquisado

# grupo regex com dois grupos separados por |
heroRegex = re.compile (r'Batman|Tina Fey') 
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo1 = heroRegex.search('Tina Fey and Batman.')
print(mo1.group())
print()