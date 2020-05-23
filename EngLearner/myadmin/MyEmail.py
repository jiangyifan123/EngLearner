import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Mail:
    def __init__(self):
        # 第三方 SMTP 服务

        self.mail_host="smtp.qq.com"       #设置服务器:这个是qq邮箱服务器，直接复制就可以
        self.mail_pass="aoncrqxglnuzbbfb"           #刚才我们获取的授权码
        self.sender = '985897924@qq.com'      #你的邮箱地址 

    def send(self, receivers = ['985897924@qq.com'], content = "", subject = '主题'):
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("发件人名字，可自由填写", 'utf-8')  
        message['To'] =  Header("收件人名字，可自由填写", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8') 
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465) 
            smtpObj.login(self.sender,self.mail_pass)  
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            smtpObj.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败')