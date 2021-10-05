# app.py - KinConnections
# Serves as main driver for KinConnections platform

import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from flask_restful import Api

from resources.auth import auth
from resources.routes import initialize_routes

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

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
