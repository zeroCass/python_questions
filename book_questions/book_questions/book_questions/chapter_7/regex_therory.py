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

heroRegex = re.compile(r'Bat(man|woman|mobile)')
print(heroRegex.findall('Batmobile lost a wheel. So, Batman wont find Batwoman'))
print()




# findall() - metodo
# quando chamado em uma ragex sem grupos - retorna uma lista de strings correspondeste
# quando chamado em uma ragex com grupos - retorna uma lista de tuples com os grupos correspondentes

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # não tem nenhum grupo
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # tem grupos
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
print()


# ponto de interrgoacao - ocorrencia opicial
# quando um trecho pode ou nao esta contido, e o resultado obtido devera ser considerado de qualquer jeito
# exemplo Bat(wo)?man - ira retornar se batman ou batwoman esta no texto
# entao o grupo (wo)? eh um grupo opcional podendo ou nao esta preesnte

batRegex = re.compile(r'(Bat|bat)(wo)?man')
print(batRegex.search('The adventures of batman').group())
print(batRegex.search('The adventures of Batwoman').group())
print()


# asteriscos - ocorrencia de zero ou mais do grupo anterior
batRegex = re.compile(r'bat(wo)*man', re.IGNORECASE)
print(batRegex.search('Batwowowoman is a woman').group())
print()

# + - ocorrencia de um ou mais do grupo anterior
batRegex = re.compile(r'bat(wo)+man', re.IGNORECASE)
print(batRegex.search('BATWOWOMAN, The Adventure').group())
print()


# grupos/itervalos personalizados usando []
vogals = re.compile(r'[aeiouAEIOU]')
print(vogals.findall('Ola senhoras e senhores'))
print()


# {} - repeticoes especificas do grupo anterior
# pode-se usar intervalos para especificar a quantiade:
#   {3,} - tem que ter no minimo 3 ou varios
#   {,3} - pode ter nenhum ou no maximo 3
#   {3, 5} - precisa ter entre 3 e 5
# *** OBS: Eh importante menconar que por default a regex irá mostrar a maior ocorrencia (greed - guloso)
#           para que isso nao aconteca, eh necessario colocar um ? apos o grupo '(Ha){3,5}?'
ha_regex = re.compile('(Ha){1,}', re.IGNORECASE)
print(ha_regex.search('HahaHAHA, estou rindo ein').group())
print()


# ^ e $ - ^ especifica que a palavra deve começar com aquela ocorrencia, em quanto que $ indica que string irá terminar
# com um padrao especifico
whole_string_is_num = re.compile(r'\d+$')
#a string devera ser somente numeros
print(whole_string_is_num.search('20021'))
print() 


#. - coringa -> corresponde a qualquer caractere que nao seja quebra de linha
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))
print() 

# metodo re.DOTALL considera o caractere de quebra de linha
new_line_regex = re.compile('.*', re.DOTALL)
print(new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print() 

# metodo sub - serve para sibstiuir a ocorrencia especifica pela string passada como param
agent_name_regex = re.compile(r'Agent (\w)(\w)\w*')
print(agent_name_regex.sub(r'\1\2***','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
#print(agent_name_regex.findall('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
print()

# ignorando espacos e comentarios para facilitar a leitura da regex -> re.VERBOSE
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # codigo area pode der ddd ou (ddd)
    (\s|-|\.)?                      # separador pode ser espaco em branco ou - ou .
    (\d{3})                         # primeiros 3 digitos
    (\s|-|\.)?                      # separador pode ser espaco em branco ou - ou .
    (\d{4})                         # ultimos 3 digitos
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extensao
)''', re.VERBOSE)
print(phoneRegex.search('(123).456.7890 x 000').group())

# combinar IGNORECASE, DOTALL e VERBOSE ->  re.compile(re.IGNORECASE | re.DOTALL | re.VERBOSE)