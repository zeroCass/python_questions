'''
modulo webbrowser
    nativo do python e abre um vanegador na pagina especifica passada 
    na funcao open()

'''
import webbrowser
import pyperclip, sys

website = 'https://www.google.com/maps/place/'

if len(sys.argv) > 1:
    # pega o valor do argumento e converte para string
    adress = ''.join(sys.argv[1:])
else:
    # pega o dado armazenado no buffer (crtl + c)
    adress = pyperclip.paste()

print(type(adress))
webbrowser.open(adress)