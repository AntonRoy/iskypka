import smtplib
import ssl
import settings
from email.mime.text import MIMEText
 
def send_email(to_addr, from_addr, password, body_text):
    msg = MIMEText(body_text.encode('utf-8'), _charset='utf-8')
    context = ssl.create_default_context()
    smtp_server = "smtp.gmail.com"
    port = 587
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        print(from_addr, password)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as e:
        print(e)
