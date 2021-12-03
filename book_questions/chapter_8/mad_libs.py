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

# verifica se o argumento tem o nome do arquivo
if len(sys.argv) < 2:
    sys.exit(1)
else:
    text_file = sys.argv[1]
    # verifica se o arquivo eh .txt
    if not '.txt' in text_file:
        print('Error: not a text file')
        sys.exit()
    
    # verifica se o arquivo existe
    if not os.path.exists(text_file):
        print('File doesnt exists')
        sys.exit()

    # cria a regex contendo os grupos com as possbilidades
    regex = re.compile('(ADJECTIVE)|(NOUN)|(ADVERB)|(VERB)')

    # abre e ler o arquivo, entao faz os tratametnos
    # obj: achar todas as oracoes (separadas por ponto) do arquivo, para exibir uma frase que faca sentido
    # para entao o usurario escolher qual palavra se encaixa melhor
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
            all_phrases.append(file_content[begin_phrase:all_dots[dot]].strip())
            # atualiza o inicio da frase como sendo a posicao do ponto + 1
            begin_phrase = all_dots[dot] + 1
        
        new_phrase = [] 
        for phrase in range(len(all_phrases)):
            # tamanho de palavras a serem subsituidas
            total_finders = len(regex.findall(all_phrases[phrase]))
            # une as frases
            current_phrase = all_phrases[phrase]

            for i in range(total_finders):

                print(f'{current_phrase}')
                # procura a primeira ocorrencia 
                match = regex.search(current_phrase).group()
                # pede para o usuario inserer o que deseja colocar no lugar
                new_word = input(str((f'\nEnter a(n) {match}:\n')))
                # substitue a palavra antiga pela palavra atual
                current_phrase = re.sub(match, new_word, current_phrase)

            current_phrase += '. '
            new_phrase.append(current_phrase)
                 
        #sub = re.sub('.txt','',text_file)
        sub = text_file.strip('.txt')
        # cria novo arquivo e salva ele
        new_txt = open(f'{sub}_new.txt','w')
        for phrase in new_phrase:
            new_txt.write(phrase)
            print(phrase)
        new_txt.close()
