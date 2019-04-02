#!/usr/bin/python

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime

def sendemail():
    user = 'test@test.com'
    pwd = 'test'
    to = ['test@test.com']
    msg = MIMEMultipart()
    msg['Subject']  = 'disk Exceed the limit, Please Process'
    msg['From'] = user
    msg['To'] = ','.join(to)
    part = MIMEText('test disk Exceed the limit, Please Process')
    msg.attach(part)

    server = smtplib.SMTP('smtp.test.com')
    server.login(user, pwd)
    server.sendmail(user, to, msg.as_string())
    server.close()


def cpu_temp():
    return os.system('sh cpu_temp.sh')
