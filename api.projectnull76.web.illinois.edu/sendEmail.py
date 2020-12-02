#coding: utf-8
import smtplib
from email.mime.text import MIMEText
import ssl

def sendEmail(targetmail, content, imageid):
    context = ssl.create_default_context()
    gmail_user = 'noreplyprojectnull@gmail.com'
    gmail_password = 'null1234'
    subject = 'Your image %s have new comment' % (imageid)

    msg = MIMEText(content,'plain', 'utf-8')

    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = targetmail

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls(context = context)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user,targetmail,msg.as_string())
        server.close()
        # print('---------------------------------------------')
        # print(msg)
        # print('---------------------------------------------')
    except smtplib.SMTPException as e:
        return 'Error info: '+ str(e)

# test function
# sendEmail("rtao6@illinois.edu", "Hello", "121314")