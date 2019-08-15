import smtplib
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
password = str(input('Please enter your password:'))
smtpObj.login('cgarrido@savers.com', password)
smtpObj.sendmail('cgarrido@savers.com', 'cgarrido@savers.com', 'Subject: Python.\nI sent this via a script. This is a test to automate cradlepoint e-mails.')
smtpObj.quit()
