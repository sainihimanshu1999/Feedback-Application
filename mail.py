import smtplib
from email.mime.text import MIMEText


def send_mail(Customer, dealer, rating, comments):
    port  = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '948ad8e6b37eab'
    password = '76712f51ddbfa7'
    message = f"<h3>New feedback submission</h3><ul><li>Customer : {Customer}</li><li>Dealer : {dealer}</li><li>Rating : {rating}</li><li>Comments : {comments}</li></ul>"

    sender_email = 'email1@example.com'
    reciever_email = 'email2@example.com'
    msg = MIMEText(message , 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From']  = sender_email
    msg['To'] = reciever_email


    with smtplib.SMTP(smtp_server , port) as server:
        server.login(login , password)
        server.sendmail(sender_email , reciever_email , msg.as_string())