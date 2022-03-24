import os
import datetime
import smtplib

from dotenv import load_dotenv
import pystache

load_dotenv()

SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASS = os.environ.get('SMTP_PASS')

SMTP_OBJ = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
SMTP_OBJ.starttls()
SMTP_OBJ.login(SMTP_USER, SMTP_PASS)


def send_email(from_address, to_address, template='template.mustache'):

    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
    subject = 'subject'

    msg = None
    with open(template, 'r') as f:
        text = f.read()
        print(text)
        msg = pystache.render(text, {
            'from': from_address,
            'to': to_address,
            'subject': subject,
            'date': date,
        })

    SMTP_OBJ.sendmail(from_address, to_address, msg)



if __name__ == '__main__':

    send_email(SMTP_USER, 'test_address@gmail.com')

    SMTP_OBJ.quit()

    print('END')