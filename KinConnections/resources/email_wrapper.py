# email_wrapper.py - KinConnections
# Serves as wrapper for sending connection emails

# for environment variables
import os
from dotenv import load_dotenv
# for email engine
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# for rich html email
from dominate import document
from dominate.tags import *
# flask
from flask import Blueprint, Response, request, render_template, session, redirect, url_for, jsonify
from flask_restful import Resource
# database
from .db_wrapper import db_wrapper


os.getenv("SENDGRID_API_KEY")

class Email(Resource):
    def post(self, id):
        # ensure logged in
        if not session.get('email', None):
            return 'Unauthorized Access', 401

        # send email
        user_subject = request.form.get('userSubject')
        user_message = request.form.get('userMessage')

        currentConnector = db_wrapper.get_connector_by_id(id)
        connector_name = (currentConnector['first_name'] + ' ' + currentConnector['last_name'])
        connector_email = (currentConnector['email'])

        sender_name = (session['first_name'] + ' ' + session['last_name'])
        sender_email = (session['email'])

        if (self.__send_email_message(sender_name, sender_email, connector_name, connector_email, user_subject, user_message)):
            return 'OK', 200
        else:
            return 'Unable to send message', 500

    def __send_email_message(self, sender_name, sender_email, recipient_name, recipient_email, message_subject, message_body):

        # Create the plain-text and HTML version
        text_string = sender_name + " would like to connect with you on KinConnections, subject: " + message_subject + " and message: " + message_body
        html_string = self.__write_html_message(sender_name, sender_email, message_subject, message_body)

        # construct mail object
        message = Mail(
            from_email = ("noreply@globalencountersprogramme.org", "Kin Connections (Global Encounters)"),
            to_emails = (recipient_email, recipient_name),
            subject = "New Connection from " + sender_name,
            plain_text_content = text_string,
            html_content = str(html_string)
        )
        message.add_cc(("connections@kc.campconnect.co", "Kin Connections"))
        message.reply_to = (sender_email,sender_name)

        # send mail
        try:
            sendgrid_client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sendgrid_client.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
            print(e.body)
            return False

        return True

    def __write_html_message(self, sender_name, sender_email, message_subject, message_body):
        with document(title="KinConnections New Connection") as html_object:
            h1('KinConnections')
            h2('New Connection from ' + sender_name)
            p('Sender Email ' + sender_email)
            hr()
            h3('Subject: %s' % message_subject)
            p('Message: %s' % message_body)
            hr()
            with span():
                p('You are receiving this email because you are a connector on Kin Connections (kc.campconnect.co)')
                p('If you wish to no longer be a connector, please email connections@kc.campconnect.co')
        return html_object