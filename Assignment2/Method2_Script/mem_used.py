#!/usr/bin/python

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    #meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

def sendemail():
    user = 'test@test.com'
    pwd = 'test'
    to = ['test@test.com']
    msg = MIMEMultipart()
    msg['Subject']  = 'Memory Exceed the limit, Please Process'
    msg['From'] = user
    msg['To'] = ','.join(to)

    part = MIMEText('Memory Exceed the limit, Please Process')
    msg.attach(part)


    server = smtplib.SMTP('smtp.test.com')
    server.login(user, pwd)
    server.sendmail(user, to, msg.as_string())
    server.close()

if __name__=='__main__':
    #print(meminfo())
    meminfo = meminfo()
    #print('Total memory: {0}'.format(meminfo['MemTotal']))
    #print('Free memory: {0}'.format(meminfo['MemFree']))
    memusage = (int(meminfo['MemTotal'].split()[0]) - int(meminfo['MemFree'].split()[0]))/int(meminfo['MemTotal'].split()[0])
    if memusage > 0.75:
        sendemail()
