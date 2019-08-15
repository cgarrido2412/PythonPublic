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
number = str(input("Which node is down?:"))
subj = "Juniper EX2200 - MGR NODE " + number
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = "Good morning team partners!\n I just wanted to reach out to let you know that during monitoring, we've detected a non-working network switch in the office.\n To cake care of this we're sending a cradlepoint troubleshooting unit that will let us log into the network switch and attempt to reconfigure it.\n \n I will update you shortly with the setup instructions and tracking number, please feel free to reach out if you have any questions!"

#source and destination e-mail addresses
from_addr = email
to_addr = str(input("Please enter who you'd like to send an e-mail to:"))

#Appending subject and message body into a single variable 
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

#Sending the e-mail. Having netadmins@savers.com as second argument BCC's team
blindcopy = str(input('Please enter an address to blind copy to:'))
smtpObj.sendmail(email, blindcopy, msg)
smtpObj.quit()
