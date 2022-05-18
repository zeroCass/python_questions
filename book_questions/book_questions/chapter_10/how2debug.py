'''
Debbugin:

raise Excepetion('Mensagem')
Caso não haja um try/exception para tratar ou cuidar dessa exceção, o programa falhará

trackback
Eh uma mensagem que contém detalhes do erro ocorrido, como a linha que falhou, etc
Tabmem possui uma sequencia de chamadas que provocou esse erro (call stack)
Podemos obter trackback sem que o programa falhe com o modulo import traceback
    *trackback.forrmat_exec() -> retorna string contendo informacoes sobre o erro

assertion
verficiacao de sanidade do codigo, serve para fazer um teste booleano em uma situacao no codigo
Se houver erro, este sera exibido decorrente da falha na execucao
    assert <avalicao booleana>('mensagem de erro a ser exibida')
A assertion nao devera ser tratada, ou seja, caso ocorra o erro, o programa deve FALHAR

*Assertion vs Exception:
    Assertion informa que um bug deve ser corrigido em quanto que uma exeception podem ser tratadas
    e portanto pode haver ma recuperacao (ex: arquivo nao encontrado ou  dados invalidos)

Logging
*modulo logging
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
Com a funcao logging.debug('mensagem') eh possivel exibir valores de variaveis e informacoes uteis assim como
o print

Print vs Logging
Eh possivel desabilitar todos os logs com a funcao logging.disable(logging.CRITICAL(esse eh o tipo de log a desabilitar)),
assim nao precisa apagar um a um os prints.
Existem niveis de logging:
    -debug
    -info
    -warning
    -error
    -critical
*Salvar log em arquivo de texto:
    logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s
- %(levelname)s - %(message)s')

'''

