from aicansell import settings

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    bg_color = '#f0f0f0'
    html_body = f'<html><body style="background-color: {bg_color};">{body}</body></html>'
    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attachment_path, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def send_added_words_update():
    sender_email = settings.EMAIL_HOST_USER
    sender_password = settings.EMAIL_HOST_PASSWORD
    receiver_email = 'kritgyakumar92@gmail.com'
    subject = 'Words Excel File'
    body = 'Please find attached the Excel file.'
    attachment_path = 'words.xlsx'
    send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
