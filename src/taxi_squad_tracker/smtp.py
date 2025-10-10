import smtplib
from email.mime.text import MIMEText

from .config import config

SMTP_SERVER = config.smtp.server
SMTP_PORT = config.smtp.port
EMAIL = config.smtp.email
PASSWORD = config.smtp.password


def send_email(recipient: str, message: str):
    msg = MIMEText(message)
    msg["From"] = EMAIL
    msg["To"] = recipient
    msg["Subject"] = "Taxi Squad Enforcement"
    print(msg)
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, [recipient], msg.as_string())
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send Email to {recipient}: {e}")
