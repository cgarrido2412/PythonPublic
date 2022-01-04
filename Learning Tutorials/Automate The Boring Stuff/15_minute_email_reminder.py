#Script will wait 15 minutes, then send an e-mail reminder to check in on things. 

#imports for code to function
#open cli and navigate to C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\Scripts>
#use "pip install MODULE" to install 
from threading import Timer
import smtplib
import datetime

def timeout():
    print("Script complete.")

# duration is in seconds
t = Timer(15 * 60, timeout)
t.start()

# wait for time completion
t.join()

#Connecting to outlook smtp server and establishing tls session
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

#login and authentication
email = 'REDACTED'
password = 'REDACTED'
password = password.strip()
smtpObj.login(email, password)

#Defining subject and message body
subj = "REDACTED"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = "This is a test script, I figure if we're busy and we're troubleshooting multiple things we can kick off this script and it'll remind us to check on a switch after 15 minutes. \n It has been 15 minutes since the switch has been power cycled. Please check on its status."

#source and destination e-mail addresses
from_addr = email
to_addr = 'REDACTED'

#Appending subject and message body into a single variable 
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

#Sending the e-mail. Having someemail@email.com as second argument BCC's team
blindcopy = 'REDACTED'
smtpObj.sendmail(email, blindcopy, msg)
smtpObj.quit()
