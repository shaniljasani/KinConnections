# email_wrapper.py - KinConnections
# Serves as wrapper for sending connection emails

import os
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# access credentials from .env
load_dotenv(dotenv_path="../.env")

kc_email = os.getenv("KC_EMAIL")
kc_email_password = os.getenv("KC_EMAIL_PASSWORD")
kc_email_server = os.getenv("KC_EMAIL_SERVER")
kc_email_port = int(os.getenv("KC_EMAIL_PORT"))

def send_email_message(sender_name, sender_email, recipient_name, recipient_email, message_subject, message_body):
    
    message = MIMEMultipart("alternative")

    message['Subject'] = "[KinConnections] New Connection from " + sender_name
    message['From'] = formataddr(("Kin Connections", "connections@kc.campconnect.co"))
    message['Reply-To'] = formataddr((sender_name, sender_email))
    message['Cc'] = formataddr(("Kin Connections", "connections@kc.campconnect.co"))
    message['To'] = formataddr((recipient_name, recipient_email))


    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Kin Connections is awesome:
    www.campconnect.co"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.campconnect.co">KINConnections</a> 
        is <strong>awe</strong>some.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(kc_email_server, kc_email_port, context=context) as server:
        server.login(kc_email, kc_email_password)
        server.send_message(message)
    
    return True