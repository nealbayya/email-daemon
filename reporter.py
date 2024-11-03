import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email configuration
SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
TO_ADDRESS = os.environ.get('TO_ADDRESS')
SUBJECT = 'Weekly report'
BODY = 'TODO'


def send_email():
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = SUBJECT

    # Attach the body with the msg instance
    msg.attach(MIMEText(BODY, 'plain'))

    # Create SMTP session for sending the mail
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Enable security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print('Email sent successfully!')

if __name__ == '__main__':
    send_email()