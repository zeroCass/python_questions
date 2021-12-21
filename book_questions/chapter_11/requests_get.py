
import requests, os

# muda o dir para a pasta de trabalho  arquivo do arquivo atual
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# retorna um objeto request
# o metodo get ira acessar uma url e fazer uma requiscao para ele. 
# a resposta sera o conteudo da pagina baixado com string para var
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# gera um erro caso a solicitacao da pagina n seja bem sucedida
res.raise_for_status()

# requests.codes.ok verifica que a comunicao com a pagina foi bem sucedida
if res.status_code == requests.codes.ok:
    print(len(res.text))
    print(res.text[:250])

# apesar de pode exibir o conteudo do site com a fucao .text(), 
# eh recomendo salvar em binario para preservar a codificao unicode do texto da pagina
with open(os.path.join(os.getcwd(), 'RomeoAndJuliet.txt'), 'wb') as file:
    
    # iter_content() retorna porcoes de um dado
    # isso evitar de sobrecarregar a memoria do programa ao gravar um dado no disco
    for chunk in res.iter_content(100000):
        file.write(chunk)