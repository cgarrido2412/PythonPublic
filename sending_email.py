import smtplib
import datetime
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
password = str(input('Please enter your password:'))
smtpObj.login('cgarrido@savers.com', password)
subj = "TEST - Juniper EX2200 - MGR NODE - Cradlepoint Troubleshooting"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = "Good morning team partners!\n I just wanted to reach out to let you know that during monitoring, we've detected a non-working network switch in the office.\n To cake care of this we're sending a cradlepoint troubleshooting unit that will let us log into the network switch and attempt to reconfigure it.\n \n I will update you shortly with the setup instructions and tracking number, please feel free to reach out if you have any questions!"
from_addr = "Charles Garrido <cgarrido@savers.com>"
to_addr = "charles.garrido@gmail.com"
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )
#Having netadmins@savers.com as second argument BCC's team
smtpObj.sendmail('cgarrido@savers.com', 'netadmins@savers.com', msg)
smtpObj.quit()
