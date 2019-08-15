import smtplib
import datetime
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
password = str(input('Please enter your password:'))
smtpObj.login('cgarrido@savers.com', password)
subj = "Whatever you want the subject of your e-mail to be"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = "Whatever you want the message body to be."
from_addr = "Charles Garrido <cgarrido@savers.com>"
to_addr = "someaddress@provider.com"
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )
#Having blindcopyaddress@savers.com as second argument BCC's address
smtpObj.sendmail('cgarrido@savers.com', 'blindcopyaddress@savers.com', msg)
smtpObj.quit()
