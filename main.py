import smtplib
from email.mime.text import MIMEText
import os,time
su_old=24

def get_token():
	
	return 666
def faemeil(xxx='默认'):
		subject = "贴吧签到通知"
		content = f"<h4>{xxx}</h4>"  # 邮件内容
		sender = "18381801393@163.com"  # 发件人
		password = 'NNKJXXRPAOGGLTMP'  # 刚才我们在163邮箱里设置的授权密码
		receivers = ["1019157263@qq.com"]  # 收件人
		for receiver in receivers:
		    message = MIMEText(content, "html", "utf-8")
		    message["From"] = sender
		    message["To"] = receiver
		    message["Subject"] = subject
		 
		    smtp = smtplib.SMTP_SSL('smtp.163.com', 994)
		    smtp.login(sender, password)
		    smtp.sendmail(sender, [receiver], message.as_string())
		    smtp.close()
if __name__ == "__main__":
	faemeil("github_actions_send_email")
	print(666)
