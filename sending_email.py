import smtplib
import datetime
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
password = str(input('Please enter your password:'))
smtpObj.login('cgarrido@savers.com', password)

subj = "Cradlepoint"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = "Hello\n This is letting you know you'll be receiving a cradlepoint.\n Have a nice day!"
from_addr = "Charles Garrido <cgarrido@savers.com>"
to_addr = "netadmins@savers.com"
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

smtpObj.sendmail('cgarrido@savers.com', 'netadmins@savers.com', msg)
smtpObj.quit()
