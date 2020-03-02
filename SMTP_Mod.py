#This is the module for SMTP
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"
mail_user = "circles2020@163.com"
mail_pass = "SRF135ii"

sender = 'circles2020@163.com'
receivers = ['circles2020@163.com']
 
message = MIMEText('today...','plain','utf-8')

message['From'] = Header("rooster",'utf-8')
message['To'] = Header("test",'utf-8')

subject = 'rooster'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtp0bj = smtplib.SMTP()
    smtp0bj.connect(mail_host, 25)
    smtp0bj.login(mail_user, mail_pass)
    smtp0bj.sendmail(sender, receivers, message.as_string())
    print("1")

except smtplib.SMTPException:
    print("2")
        
