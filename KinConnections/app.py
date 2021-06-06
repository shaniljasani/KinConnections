import os

from flask import Flask, render_template, session
from auth.auth import auth_bp
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.getenv("APP_SECRET")
app.register_blueprint(auth_bp)

# redirect on trailing slashes
@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path 
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# the home/main page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")


newDemoProfile = {
    "first_name" : "Kabir",
    "last_name" : "Barday",
    "email" : "ceo@kc.com",
    "password" : "demopass",
    "dob" : "37257",
    "country_origin" : "USA",
    "region_current" : "USA",
    "location_current" : "Bay Area, CA",
    "gender" : "male",
    "languages" : ["English", "Hindi/Urdu"],
    "acknowledgement" : "TRUE",
    "user_type" : "Connector",

    "title" : None,
    "professional_category" : ["Business", "Technology"],
    "education" : {"School0Name" : "UT Austin", "School0Major" : "ECE"},
    "linkedin" : "https://linkedin.com/in/kabir",
    "bio" : "hi my name is pickles",
    "images" : ["/static/img/users/shanil.jpg"],
    "approved" : "TRUE",
}

@app.route('/connector/<connector_name>')
def connector_profile(connector_name):
    return render_template("connector.html", connector=newDemoProfile)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)