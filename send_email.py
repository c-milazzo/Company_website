import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "milazzo.chris1@gmail.com"
    mail_pass = "pvtqopaplkomswdj"

    receiver = "milazzo.chris1@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, mail_pass)
        server.sendmail(username, receiver, message)
