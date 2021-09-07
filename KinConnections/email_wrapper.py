# email_wrapper.py - KinConnections
# Serves as wrapper for sending connection emails

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# TODO place in .env
kc_email = "connections@kc.campconnect.co"
kc_email_password = 'SjFf2021!'

def send_email(sender_name, sender_email, recipient_name, recipient_email):
    
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
    with smtplib.SMTP_SSL("box2030.bluehost.com", 465, context=context) as server:
        server.login(kc_email, kc_email_password)
        server.send_message(message)
    

# send_email('Shanil', 'shaniljasani+send@gmail.com', 'Shanil Jasani', 'shaniljasani+receive@gmail.com')