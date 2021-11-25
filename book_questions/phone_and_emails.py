'''
Livro - Automatize Tarefas Macantes com Python by Al Sweigart
Capitulo 7

Projeto: extrator de números de telefone e de
endereços de email

Suponha que você tenha a tarefa maçante de localizar todos os números de
telefone e endereços de email em uma página web ou um documento extenso.
Se fizer rolagens manualmente pela página, você poderá acabar fazendo a
208
pesquisa por bastante tempo. Porém, se você tivesse um programa que
pudesse pesquisar o texto em seu clipboard em busca de números de telefone
e de endereços de email, seria possível simplesmente pressionar CTRL-A para
selecionar todo o texto, CTRL-C para copiá-lo para o clipboard e então
executar o seu programa. Ele poderia substituir o texto no clipboard somente
pelos números de telefone e pelos endereços de email encontrados.

Adicional (next_feature):
É possivel passar um arquivo .txt para o programa.
Ele irá procurar esse arquivo e extrair os dados requiridos. Posteriormente, irá gerar um novo
arquivo .txt contendo os dado extraidos
'''


import sys, os
import pyperclip, re


def get_file(file_name):
    ''' 
        this function will serach the file in the main dir  
        or in another dir in the main dir.
        return: file_path
    '''
    # get the dir path of current pathname module
    dir_base = os.path.dirname(os.path.abspath(__file__))

    # check if the file exist in the current dir
    if os.path.exists(dir_base + '\\' + file_name):
        return os.path.join(dir_base, file_name)

    # check if the file exists in other dir in the main dir
    for dir in os.listdir(dir_base):
        if not os.path.isfile(dir):
            if os.path.exists(os.path.join(dir_base, dir, file_name)):
                return os.path.join(dir_base, dir, file_name)
    return None






def phone_list (text: str) -> list:
    '''
        regex that return the phone list
    '''
    phones = re.compile(r'''(
        (\d{2,3}|\(\d{2,3}\))               # codigo area pode der ddd ou (ddd)
        (\s|-|\.)?                      # separador pode ser espaco em branco ou - ou .
        (\d{5})                         # primeiros 3 digitos
        (\s|-|\.)?                      # separador pode ser espaco em branco ou - ou .
        (\d{4})                         # ultimos 3 digitos
        (\s*(ext|x|ext.)\s*\d{2,5})?    # extensao
    )''', re.VERBOSE)
    # seach for phones number in the text
    phone_l = phones.findall(text)

    # the return is a list of tuples
    # so get the first element in the tuple wich is the complete numbe
    # and put in the list
    new_list = []
    for tuple in phone_l:
        new_list.append(tuple[0])
    return new_list



def emails_list (text: str) -> list:
    ''' this function will extract all emails from a text '''
    emails = re.compile(r'''(
        ([a-zA-Z0-9._%+-]+)             # nome de usuario
        @                               # simbolo @ obrigatorio
        ([a-zA-Z0-9._%+-]+)             # dominio
        (\.[a-zA-Z]{2,5})               # ponto seguindo por mais caracteres
        ((\.[a-zA-Z]{2,5}))?
        ((\.[a-zA-Z]{2,5}))?
    )''', re.VERBOSE)
    # seach for emails in the text
    emails_l = emails.findall(text)

    # the return is a list of tuples
    # so get the first element in the tuple wich is the complete numbe
    # and put in the list
    new_list = []
    for tuple in emails_l:
        new_list.append(tuple[0])
    return new_list



def main ():
    if len(sys.argv) < 2:
        text = pyperclip.paste()
        phones_list = phone_list(text)

        phones_text = 'Phones:\n'
        phones_text += '\n'.join(phones_list)

        email_list = emails_list(text)
        emails_text = 'Emails:\n'
        emails_text += '\n'.join(email_list)

        final_text = phones_text + '\n\n' + emails_text
        pyperclip.copy(final_text)

    else:
        file = get_file(sys.argv[1])
        try:
            with open(file) as file:
                print(file.read())
        except Exception as e:
            print(e)
    



if __name__ == '__main__':
    main()
    