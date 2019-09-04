#!/usr/bin/python

import smtplib

sender = 'REDACTED@DOMAIN.com'
receivers = ['REDACTED@DOMAIN.com']

message = """From: ALIAS <REDACTED@DOMAIN.com>
To: FIRST LAST <REDACTED@DOMAIN.com>
Subject: TEST

BODY
"""

try:
   smtpObj = smtplib.SMTP('smtpi.DOMAIN.com')
   smtpObj.sendmail(sender, receivers, message)         
   print( "Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
