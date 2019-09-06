import smtplib
from email.mime.text import MIMEText
msg_from='669293657@qq.com'                                 #发送方邮箱
passwd='kqpathdrxwjlbeig'                                   #填入发送方邮箱的授权码
msg_to='669293657@qq.com'                                       #收件人邮箱

subject="域名解析警告"                                     #主题
content="域名暂不可用,请检查配置~"                          #内容
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)                               #登录SMTP服务器
    s.sendmail(msg_from, msg_to, msg.as_string())#发邮件 as_string()把MIMEText对象变成str
    # print ("发送成功")
except s.SMTPException:
    # print ("发送失败")
    pass
finally:
    s.quit()
