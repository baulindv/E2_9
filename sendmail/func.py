from email.header import Header
from email.mime.text import MIMEText
from random import choice
import threading
import smtplib

EMAIL_QUEUE = []
QUEUE_SIZE = 10


rambler_login = 'sf_dz_e2_baulindv@rambler.ru'
rambler_password = 'lhdfjkLGkygdf89ydfJHG'
rambler_smtp = 'smtp.rambler.ru'
rambler_port = 465


EMAIL_FROM = 'sf_dz_e2_baulindv@rambler.ru'

# Не обязательно, удобно для тестирования
EMAIL_TO = ''


def send_email(*args):
    smtp_server = smtplib.SMTP_SSL(rambler_smtp, rambler_port)
    smtp_server.login(rambler_login, rambler_password)

    msg = MIMEText(args[2], _charset="UTF-8")
    msg['Subject'] = Header(args[1], 'utf-8')

    smtp_server.sendmail(EMAIL_FROM, args[0], msg.as_string())
    smtp_server.close()


# !!!!!!!!!!!!Переделано на прямую отправку через SMTP так как были проблемы с аккаунтом SendGrid
# SENDGRID_API_KEY = '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'
# def send_email(*args):
#     m = Mail(from_email=EMAIL_FROM,
#              to_emails=args[0],
#              subject=args[1],
#              html_content=f'<b>{args[2]}</b>')
#     try:
#         sg = SendGridAPIClient(SENDGRID_API_KEY)
#         response = sg.send(m)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e)


def random_num(num):
    return choice(range(1, num))


def worker(*args):
    send_email(*args)


def add_email_to_queue(email, subject, text, delay):
    t = threading.Timer(delay, worker, args=(email, subject, text,))
    t.start()
    EMAIL_QUEUE.append({'email': email, 'params': [subject, text, delay]})


def list_email_queue():
    return EMAIL_QUEUE[-QUEUE_SIZE:]

if __name__ == '__main__':
    send_email()