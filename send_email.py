import smtplib, ssl
from email.mime.text import MIMEText


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "oseghaleokononfua@gmail.com"
    password = "hdfm jcqd pivf envz"

    receiver = "oseghaleokononfua@gmail.com"
    # context = ssl.create_default_context()

    # Create MIME email (UTF-8)
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "Today's News Update"
    msg["From"] = username
    msg["To"] = receiver

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # server.sendmail(username, receiver, message)
        server.send_message(msg) 
        

# send_email("Hello, how are you?")
