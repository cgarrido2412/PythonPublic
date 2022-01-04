import smtplib
import datetime

#Connecting to outlook smtp server and establishing tls session
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

#login and authentication
email = str(input('Please enter your e-mail:'))
password = str(input('Please enter your password:'))
smtpObj.login(email, password)

#Defining subject and message body
subj = str(input('Subject:'))
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = str(input('Message:'))

#source and destination e-mail addresses
from_addr = email
to_addr = str(input("Please enter who you'd like to send an e-mail to:"))

#Appending subject and message body into a single variable 
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

#Sending the e-mail. Having blindcopy defined will send BCC e-mail
blindcopy = str(input('Please enter an address to blind copy to:'))
smtpObj.sendmail(email, blindcopy, msg)
smtpObj.quit()
