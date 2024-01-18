import smtplib

from aicansell.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
from pathlib import Path

def send_email(subject, body, to_email, attachment_path):
    smtp_server = EMAIL_HOST
    smtp_port = EMAIL_PORT
    smtp_username = EMAIL_HOST_USER
    smtp_password = EMAIL_HOST_PASSWORD

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name='Word_Data.xlsx')
        part['Content-Disposition'] = f'attachment; filename={attachment_path.name}'
        msg.attach(part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
    print(f"Email sent to {to_email}")

def send_monthly_email():
    excel_file_path = Path('Word_Data.xlsx')

    current_month_year = datetime.now().strftime('%Y-%m')

    subject = f'Monthly Report - {current_month_year}'
    body = 'Monthly report attached.'

    send_email(subject, body, 'kritgyakumar92@gmail.com', excel_file_path)
