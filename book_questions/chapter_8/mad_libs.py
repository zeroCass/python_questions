'''
Capitulo 8 - LENDO E ESCREVENDO EM ARQUIVOS
Projeto: Mad Libs

Crie um programa Mad Libs que leia arquivos-texto e permita que o usuário
acrescente seus próprios textos em qualquer local em que a palavra
ADJECTIVE, NOUN, ADVERB ou VERB aparecer no arquivo-texto. Por
exemplo, um arquivo-texto poderá ter o seguinte aspecto:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by
these events.
O programa deve localizar essas ocorrências e pedir que o usuário as
substitua.
'''

import sys, os, re

if len(sys.argv) < 2:
    sys.exit(1)
else:
    text_file = sys.argv[1]
    if not '.txt' in text_file:
        print('Error: not a text file')
        sys.exit()
    
    if not os.path.exists(text_file):
        print('File doesnt exists')
        sys.exit()

    regex = re.compile('(ADJECTIVE)|(NOUN)|(ADVERB)|(VERB)')
    with open(text_file,'r') as file:
        file_content = file.read()

        # list of all dots index  
        all_dots = []
        for match in re.finditer('\.', file_content):
            # adiciona o idx do ponto dentro da lista
            all_dots.append(match.start())

        all_phrases = []
        begin_phrase = 0
        for dot in range(len(all_dots)):
            # adiciona uma substring da posicao do inicio da frase ate o proximo ponto
            all_phrases.append(file_content[begin_phrase:all_dots[dot]].strip().replace('\n', ' '))
            # atualiza o inicio da frase como sendo a posicao do ponto + 1
            begin_phrase = all_dots[dot] + 1

        # count = 1
        # for line in file:
        #     if regex.search(line):
        #         print('Line.%s: %s' % (count, line))
        #     count += 1