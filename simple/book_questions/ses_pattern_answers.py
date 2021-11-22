# programa para copir para a area de transferencia textos padros para ser enviado em
# em respostas de chamados ses

ANSWERS = {'reset': '''Prezados!

Foi realizado uma limpeza dos trabalhos pendentes da impressora no Server de Impressão, reconfigurado a impressora e esta voltou a operar normalmente ficando ativa e aguardando novos trabalhos de impressão.

Caso sua solicitação não tenha sido atendida satisfatoriamente, favor interagir neste mesmo chamado. Para nova(s) demanda(s), favor abrir novo chamado.

Atenciosamente,

Mateus Valério Fernandes
Estagiário
CTINF/DSI/GDAD
Telefone: 2017-1145 Ramal: 1068 '''}

import pyperclip
pyperclip.copy(ANSWERS['reset'])
