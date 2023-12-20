#Monitor Disk Usage and Send Alerts:

import psutil
import smtplib
from email.mime.text import MIMEText

def check_disk_usage_and_send_alert(threshold_percent, email_to):
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > threshold_percent:
        send_alert_email(f"Disk usage is {disk_usage.percent}%.", email_to)

def send_alert_email(message, to_email):
    from_email = "your-email@gmail.com"
    password = "your-email-password"

    msg = MIMEText(message)
    msg['Subject'] = 'Disk Usage Alert'
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# Example usage:
check_disk_usage_and_send_alert(threshold_percent=90, email_to='admin@example.com')
