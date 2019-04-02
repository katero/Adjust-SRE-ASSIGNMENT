#!/usr/bin/python

import os
import socket
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
def sendmail():
    user = 'test@test.com'
    pwd = 'test'
    to = ['test@test.com']
    msg = MIMEMultipart()
    msg['Subject']  = 'CPU Exceed the limit, Please Process'
    msg['From'] = user
    msg['To'] = ','.join(to)

    part = MIMEText('CPU Exceed the limit, Please Process')
    msg.attach(part)


    server = smtplib.SMTP('smtp.test.com')
    server.login(user, pwd)
    server.sendmail(user, to, msg.as_string())
    server.close()

def load_stat():
    loadavg = {}#dictionary

    f = open("/proc/loadavg")
    #python read file, get list split by space
    con = f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    loadavg['nr']=con[3]
    loadavg['last_pid']=con[4]
    return loadavg
#print("loadavg",load_stat()['lavg_15'])

if __name__ == '__main__':
    if load_stat()['lavg_15'] > 2.8:#4 times cpu
        sendmail()
