import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '584434525@qq.com'
mail_host = "smtp.qq.com"
mail_port = 465
mail_user = "584434525@qq.com"
mail_pass = "ktyugtjjrmbbbgae"

def csv_read_by_dict():
    with open('email.csv',encoding='utf8') as fd:
        reader=csv.reader(fd)
        headers = next(reader)
        print(headers)
        for row in reader:
            post_email(row[1],row[2],row[3])
            print(row[0],row[1],row[2],row[3])

def post_email(receivers,title, context):
    message = MIMEText(context, 'plain', 'utf-8')
    message['From'] = Header(sender)
    message['To'] = Header(str(";".join(receivers)))
    message['Subject'] = Header(title)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        return 1
    except smtplib.SMTPException:
        return None

if __name__ == '__main__':
    csv_read_by_dict()