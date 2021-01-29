from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 邮箱
form_addr = '2766801998@qq.com'
# 不是邮箱密码,而是开启SMTP服务时的授权码
password = 'gnyieacogsbmdeic'
# 收件人的邮箱
to_addr = '13012889804@163.com'
# qq邮箱的服务器地址
smpt_server = 'smtp.qq.com'

# 设置邮件信息
msg = MIMEText('每日一报啦', 'plain', 'utf-8')
msg['From'] = _format_addr('每日一报啦 <%s>' %form_addr)
msg['To'] = _format_addr('每日一报啦 <%s>' %to_addr)
msg['Subject'] = Header('每日一报啦', charset='utf-8').encode()

# 发送邮件
server = smtplib.SMTP(smpt_server, port=25)
server.set_debuglevel(1)
server.login(form_addr, password)
server.sendmail(form_addr, [to_addr], msg.as_string())
server.quit()
