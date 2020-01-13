#!/usr/bin/env python
import smtplib
from threading import Timer

def timeout():
    print("Your tea is ready.")

try:    
    steep_time = int(input('How many minutes would you like to steep your tea?\n'))
    t = Timer(steep_time * 60, timeout)
    t.start()
    t.join()
    sender = 'REDACTED'
    to_address = 'REDACTED'
    receivers = [to_address]
    message = """From: REDACTED <REDACTED>
    To: REDACTED <REDACTED>
    Subject: Tea Time
    
    Your tea is ready!
    
    Yours,
    REDACTED
    """

    try:
       smtpObj = smtplib.SMTP('COMPANY_SMTPI_SERVER')
       smtpObj.sendmail(sender, receivers, message)         
       print( "Successfully sent email")
       
    except SMTPException:
       print ("Error: unable to send email")

except KeyboardInterrupt:
    print('Program terminated.')
