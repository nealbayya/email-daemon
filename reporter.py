import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email configuration
SMTP_SERVER = 'smtp.your_email_provider.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
TO_ADDRESS = 'recipient@example.com'
SUBJECT = 'Daily Report'
BODY = 'Please find attached the daily report.'

# File to send
ATTACHMENT_PATH = 'path/to/your/report.pdf'

def send_email():
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = SUBJECT

    # Attach the body with the msg instance
    msg.attach(MIMEText(BODY, 'plain'))

    # Open the file to be sent
    with open(ATTACHMENT_PATH, 'rb') as attachment:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(attachment.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(ATTACHMENT_PATH)}')
        msg.attach(mime_base)

    # Create SMTP session for sending the mail
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Enable security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print('Email sent successfully!')

if __name__ == '__main__':
    send_email()