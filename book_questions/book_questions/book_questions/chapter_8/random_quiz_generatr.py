'''
Capitulo 8 - LENDO E ESCREVENDO EM ARQUIVOS

Projeto: gerando arquivos aleatórios de provas

Suponha que você seja um professor de geografia, tenha 35 alunos em sua
classe e queira aplicar uma prova surpresa sobre as capitais dos estados norteamericanos.
Infelizmente, sua classe tem alguns alunos desonestos, e não é
possível confiar neles acreditando que não vão colar. Você gostaria de deixar
a ordem das perguntas aleatória para que cada prova seja única, fazendo com
que seja impossível para alguém copiar as respostas de outra pessoa. É claro
que fazer isso manualmente seria uma tarefa demorada e maçante.
Felizmente, você conhece um pouco de Python.
Eis o que o programa faz:
• Cria 35 provas diferentes.
• Cria 50 perguntas de múltipla escolha para cada prova em ordem aleatória.
• Fornece a resposta correta e três respostas incorretas aleatórias para cada
pergunta em ordem aleatória.
• Grava as provas em 35 arquivos-texto.
• Grava os gabaritos contendo as respostas em 35 arquivos-texto.
Isso significa que o código deverá fazer o seguinte:
• Armazenar os estados e suas capitais em um dicionário.
• Chamar open(), write() e close() para os arquivos-texto contendo as provas e
os gabaritos com as respostas.
• Usar random.shuffle() para deixar a ordem das perguntas e as opções de
múltipla escolha aleatórias.
'''


import random, sys, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North'
'Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':
'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# cria uma varaivel que armazena o path do arquivo .py atual
main_dir = os.path.dirname(os.path.abspath(__file__))

# verifica se o dir prova_files existe, se nao, cria ele
if not os.path.exists(os.path.join(main_dir, 'provas_files')):
    os.mkdir(os.path.join(main_dir, 'provas_files'))


# gera 35 arquivos contendo as provas
for quizNum in range(35):
    # cria os arquivos com as provas e os gabaritos das respostas
    prova = open(os.path.join(main_dir, 'provas_files', f'capitals_quiz_{quizNum + 1}.txt'), 'w')
    gabarito = open(os.path.join(main_dir, 'provas_files', f'capitals_answers_{quizNum + 1}.txt'), 'w')

    # escreve o cabeçalho 
    prova.write('Name:\n\nDate:\n\nPeriod:\n\n')
    prova.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})\n\n')

    # pega uma lista contendo somente as capitais
    states = list(capitals.keys())
    # randomiza a lista
    random.shuffle(states) 

    # percorre todos os 50 estados, criando um pergunta para cada um
    for question_num in range(50):
        # obtem a resposta correta de acordo com a key do dicionario
        correct_answer = capitals[states[question_num]]

        #obtem 3 respostas erradas
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)    # remove a resposta correta da lista
        answers_options = random.sample(wrong_answers, 3) + [correct_answer]
        random.shuffle(answers_options)   # faz com que as perguntas tem ordem aleatorias

        # grava a pergunta no arquivo
        prova.write(f' {question_num + 1}. What is the capital of {states[question_num]}?\n')

        # grava as opcoes de resposat no arquivo da prova
        for i in range(4):
            prova.write('   %s. %s\n' % ('ABCD'[i], answers_options[i]))
        prova.write('\n')
    
        # grava o gabarito com as respostas corretas em um arquivo
        gabarito.write('%s. %s\n' % (question_num + 1, 'ABCD'[answers_options.index(correct_answer)]))
    prova.close()
    gabarito.close()