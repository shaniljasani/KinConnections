# app.py - KinConnections
# Serves as main driver for KinConnections platform

import os

from flask import Flask, render_template, session, request, redirect, url_for, Response
from dotenv import load_dotenv

from resources.auth import auth
from flask_restful import Api
from resources.routes import initialize_routes

from email_wrapper import *

load_dotenv(dotenv_path="../.env")

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.getenv("APP_SECRET")

app.url_map.strict_slashes = False
api = Api(app)

initialize_routes(api)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    error = request.args.get('error')
    if session.get('email', None):
        return render_template("home.html", error=error)
    else:
        return redirect(url_for("login", error=error))


@app.route('/send_email/<id>', methods=['GET', 'POST'])
def send_email(id):
    # ensure logged in
    if not session.get('email', None):
        return redirect("/login?error=notSignedIn")

    # ensure proper POST request
    if request.method != 'POST':
        return 'Error! Return <a href="/">Home</a>'

    # send email
    subject = (request.form.get('userSubject'))
    message = (request.form.get('userMessage'))

    currentConnector = get_connector_by_id(id)
    connector_name = (currentConnector['first_name'] + ' ' + currentConnector['last_name'])
    connector_email = (currentConnector['email'])

    sender_name = (session['first_name'] + ' ' + session['last_name'])
    sender_email = (session['email'])

    if (send_email_message(sender_name, sender_email, connector_name, connector_email, subject, message)):
        return "OK"
    else:
        return "Message not sent!"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)