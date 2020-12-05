#coding: utf-8
import smtplib
from email.mime.text import MIMEText


def sendEmail(targetmail, content, imageid):
    gmail_user = 'noreplyprojectnull@gmail.com'
    gmail_password = 'null1234'
    subject = 'Your image %s have new comment' % (imageid)

    msg = MIMEText(content,'plain', 'utf-8')

    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = targetmail

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user,targetmail,msg.as_string())
        server.close()
        return True
        # print('---------------------------------------------')
        # print(msg)
        # print('---------------------------------------------')
    except smtplib.SMTPException as e:
        return 'Error info: '+ str(e)

# test function
# sendEmail("binyaoj2@illinois.edu", "你好: 你在拉屎嘛？", "121314")