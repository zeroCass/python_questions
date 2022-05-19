import sys
import smtplib
import time
from email.message import EmailMessage

# cria uma conexao SMTP
try:
    gmail_handler = smtplib.SMTP('smtp.gmail.com', 587)
    print('Connection succes')
    # faz uma apresentacao para o servidor SMTP
except Exception as e:
    print(e)


gmail_handler.ehlo()
# coloca a conexão com o servidor em TLS (Modo criptografado)
gmail_handler.starttls()

user_info = input('Enter your email and password:')
user = user_info.split()

try:
    # realiza autenticacao com o servidor dado usuario e senha
    gmail_handler.login(user[0], user[1])
    print('Login succeful')
except Exception as e:
    print(e)

recv = input('Type all the recipients separete by spaces: ')
recv = recv.split()
subject = input('Type the subjetct of the mensagem:')
print('\nSignlin the end of the msg by typing --.\nType the mensage:\n')

msg = ''
# ler dados do termina ate receber -- 
for line in sys.stdin:
    msg +=  line
    if '--' in msg: break
print(msg)

# trata a mensagem 
msg = msg.replace('--', ' ')

# cria obj EmalMessage para compor uma mensasgem
mail_msg = EmailMessage()
mail_msg['Subject'] = subject
mail_msg['From'] = user[0]
mail_msg['To'] = recv
mail_msg.set_content(msg)


# existem duas formas de enviar email:
# 1 - sendmail() que recebe o email que envia, o(s) email(s) recepores e a mensagem
# 2 - send_message() que recebe um obj EmailMessage

resp = gmail_handler.sendmail(user[0], recv, f'Subject: {subject}\n{msg}')
resp = gmail_handler.send_message(mail_msg)

# x = 10
# for i in range(x):
#     resp = gmail_handler.send_message(mail_msg)
#     if len(resp) == 0:
#         print('Email send')
#     time.sleep(10)
# # print(resp)


# fecha a conexao
gmail_handler.quit()

