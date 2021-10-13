# email_wrapper.py - KinConnections
# Serves as wrapper for sending connection emails

# for environment variables
import os
from dotenv import load_dotenv
# for email engine
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
# for rich html email
from dominate import document
from dominate.tags import *
# flask
from flask import Blueprint, Response, request, render_template, session, redirect, url_for, jsonify
from flask_restful import Resource
# database
from .db_wrapper import db_wrapper


# access credentials from .env
# load_dotenv(dotenv_path="../.env")

kc_email = os.getenv("KC_EMAIL")
kc_email_password = os.getenv("KC_EMAIL_PASSWORD")
kc_email_server = os.getenv("KC_EMAIL_SERVER")
kc_email_port = int(os.getenv("KC_EMAIL_PORT"))

class Email(Resource):
    def get(self):
        return 'Error! Return <a href="/">Home</a>'
        
    def post(self, id):
        # ensure logged in
        if not session.get('email', None):
            return redirect("/login?error=notSignedIn")

        # send email
        subject = request.form.get('userSubject')
        message = request.form.get('userMessage')

        currentConnector = db_wrapper.get_connector_by_id(id)
        connector_name = (currentConnector['first_name'] + ' ' + currentConnector['last_name'])
        connector_email = (currentConnector['email'])

        sender_name = (session['first_name'] + ' ' + session['last_name'])
        sender_email = (session['email'])

        if (self.__send_email_message(sender_name, sender_email, connector_name, connector_email, subject, message)):
            resp = jsonify(success=True)
            resp.status_code = 200
            return resp
        else:
            return "Message not sent!"

    def __send_email_message(self, sender_name, sender_email, recipient_name, recipient_email, message_subject, message_body):
        
        message = MIMEMultipart("alternative")

        message['Subject'] = "[KinConnections] New Connection from " + sender_name
        message['From'] = formataddr(("Kin Connections", "connections@kc.campconnect.co"))
        message['Reply-To'] = formataddr((sender_name, sender_email))
        message['Cc'] = formataddr(("Kin Connections", "connections@kc.campconnect.co"))
        message['To'] = formataddr((recipient_name, recipient_email))


        # Create the plain-text and HTML version of your message
        text_string = sender_name + " would like to connect with you on KinConnections, subject: " + message_subject + " and message: " + message_body
        with document(title="KinConnections New Connection") as html_object:
            h1('KinConnections')
            h2('New Connection from ' + sender_name)
            hr()
            h3('Subject: %s' % message_subject)
            p('Message: %s' % message_body)
            hr()
            with span():
                # TODO use env to place domain and email
                p('You are receiving this email because you are a connector on kinconnections.com')
                p('If you wish to no longer be a connector, please email connections@kinconnections.com')

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text_string, "plain")
        part2 = MIMEText(str(html_object), "html")

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
