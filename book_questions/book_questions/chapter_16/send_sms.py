'''
Simples programa que utiliza a API da Twilio para enviar
mensagens por SMS e Whatsap
Para usar, sera necessario por no código o sid da conta e o token, assim como
o numero de telefone da twilio e o numero de telefone que recebera as mensagens
'''

import os
from twilio.rest import Client

account_sid = 'ACCOUNT_SID'
auth_token = 'TOKEN'
auth_wpp_token = 'TOKEN'
client = Client(account_sid, auth_token)

WHATSAPP_NUMBER = 'whatsapp:+14155238886'
TWILIO_NUMBER = '+19403604686'
MY_PHONE = '+'


content = 'Type the message content'

message = client.messages.create(
        body=content,
        from_= TWILIO_NUMBER,
        to=MY_PHONE
)

whatsapp_message =  client.messages.create( 
        from_='whatsapp:' + TWILIO_NUMBER,  
        body=content,      
        to='whatsapp:' + MY_PHONE 
)


print(message.sid, message.status)
print(whatsapp_message.sid, whatsapp_message.status)