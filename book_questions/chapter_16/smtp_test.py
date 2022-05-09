from cmath import log
import smtplib

gmail_handler = smtplib.SMTP('smtp.gmail.com', 587)
gmail_handler.ehlo()
gmail_handler.starttls()
login = gmail_handler.login('mateusvalerio06@gmail.com', 'mfv120SH412')
print(login)

