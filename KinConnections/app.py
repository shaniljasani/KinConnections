# app.py - KinConnections
# Serves as main driver for KinConnections platform

import os

from flask import Flask, render_template, session, request, redirect, url_for
from dotenv import load_dotenv
from db_wrapper import *

load_dotenv(dotenv_path="../.env")

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.getenv("APP_SECRET")

# redirect on trailing slashes
@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path 
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# the index public page
@app.route('/')
def index():
    return render_template("index.html")

# dashboard view for logged in users
@app.route('/home')
def home():
    if session.get('email', None):
        return render_template("home.html")
    else:
        return redirect(url_for('login'))

# user login page
@app.route('/login', methods=('GET', 'POST'))
def login():
    # user already logged in
    if session.get('email', None):
        return redirect(url_for('home'))

    # login process
    error = None
    if request.method == 'POST':
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        
        # External Authorization from function
        error = login_auth(email, password)

        # valid username == no error
        if(error == None):
            user_info = login_get_user_info(email)
            session['email'] = user_info['email']
            session['name'] = user_info['name'].lower()
            return redirect(url_for('index'))

    # else return to login page with/without error
    return render_template('login.html', error=error)

#used to logout a user
@app.route('/logout')
def logout():
    # clear cookie
    session.clear()
    # redirect to homepage
    return redirect(url_for('index'))

# signup - ask user type
@app.route('/signup')
def signup():
    if session.get('email', None):
        return render_template("home.html")
    else:
        return render_template('signup.html', type=None, error=None, success=None)


# signup - connector
@app.route('/signup/connector')
def signup_connector():
    # continue with signup process
    error = None
    success = None
    return render_template('signup.html', type="Connector", error=error, success=success)



# signup - connectee
@app.route('/signup/connectee', methods=('GET', 'POST'))
def signup_connectee():
    # user already logged in
    if (session.get('email', None)):
        return redirect(url_for('home'))
    
    # continue with signup process
    error = None
    success = None
    if request.method == 'POST':
        form_entries = {}
        form_entries['email'] = request.form.get('input_email')
        form_entries['password'] = request.form.get('input_password')
        form_entries['first_name'] = request.form.get('input_first_name')
        form_entries['last_name'] = request.form.get('input_last_name')
        form_entries['dob'] = request.form.get('input_dob')
        form_entries['nationality'] = request.form.get('input_nationality')
        form_entries['region_current'] = request.form.get('input_region_current')
        form_entries['gender'] = request.form.get('input_gender')
        form_entries['languages'] = request.form.getlist('language')
        form_entries['attended_ge'] = request.form.get('attended_ge')
        form_entries['ge_camps'] = request.form.get('input_ge_camp')
        form_entries['is_ismaili'] = request.form.get('input_is_ismaili')
        
        success, error = signup_new_connectee(form_entries)

        return render_template('signup.html', type="Connectee", error=error, success=success)    
        
    return render_template('signup.html', type="Connectee", error=error, success=success)


@app.route('/connector/<connector_name>')
def connector_profile(connector_name):
    return render_template("connector.html", connector=get_connector_by_name(connector_name))


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)