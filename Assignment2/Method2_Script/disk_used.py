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

def disk_stat():
    hd = {}
    disk = os.statvfs("/")

    disksize = disk.f_bsize * disk.f_blocks/(1024*1024*1024)
    used = disk.f_bsize * (disk.f_blocks - disk.f_bfree) / (1024 ** 3)
    hd['diskused'] = format((used / float(disksize)), '.2f')
    #return used, disksize, diskused, used1, disksize1, diskused1
    return hd

if __name__ == '__main__':
    hd = disk_stat()
    if hd['diskused'] > 0.75:
        sendemail()
