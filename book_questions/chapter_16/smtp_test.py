from cmath import log
import smtplib

gmail_handler = smtplib.SMTP('smtp.gmail.com', 587)
gmail_handler.ehlo()
gmail_handler.starttls()

user_info = input()
user = user_info.split()
gmail_handler.login(user[0], user[1])


