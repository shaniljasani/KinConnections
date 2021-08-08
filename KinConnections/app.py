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

# --------------------------------------------------------
#       AUTH FUNCTIONS
# --------------------------------------------------------

# user login page
@app.route('/login', methods=('GET', 'POST'))
def login():
    error = None

    next = request.args.get('next')

    error = request.args.get('error')
    if error == 'notSignedIn':
        error = "You must be signed in to view this page"

    # user already logged in
    if session.get('email', None):
        if next:
            return redirect('/'+next)
        return redirect(url_for('home'))

    # login process
    if request.method == 'POST':
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        
        # External Authorization from function
        error = login_auth(email, password)

        # valid username == no error
        if(error == None):
            user_info = login_get_user_info(email)
            for key in user_info.keys():
                session[key] = user_info[key]
            if next:
                return redirect('/'+next)
            return redirect(url_for('home'))

    # else return to login page with/without error
    return render_template('login.html', error=error)

#used to logout a user
@app.route('/logout')
def logout():
    # clear cookie
    session.clear()
    # redirect to homepage
    return redirect(url_for('index'))

# --------------------------------------------------------
#       REGISTRATION FUNCTIONS
# --------------------------------------------------------

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
        form_entries['region_current'] = request.form.get('input_region_current')
        form_entries['gender'] = request.form.get('input_gender')
        form_entries['languages'] = request.form.getlist('language')
        form_entries['attended_ge'] = bool(request.form.get('attended_ge'))
        form_entries['ge_camps'] = request.form.get('input_ge_camp')
        form_entries['is_ismaili'] = bool(request.form.get('input_is_ismaili'))
        
        success, error = signup_new_connectee(form_entries)

        return render_template('signup.html', type="Connectee", error=error, success=success)    
        
    return render_template('signup.html', type="Connectee", error=error, success=success)

# --------------------------------------------------------
#       CONNECTIONS FUNCTIONS
# --------------------------------------------------------

data_filters = {
    "Arts & Media" : "filter-artsmedia",
    "Business" : "filter-business",
    "Engineering" : "filter-engineering",
    "Architecture" : "filter-architecture",
    "Health & Medicine" : "filter-healthmedicine",
    "Human Resources" : "filter-humanresources",
    "International Relations, Law & Policy" : "filter-irlp",
    "Marketing & Sales" : "filter-marketingsales",
    "Non-Profit & Foundation" : "filter-nonprofit",
    "Tourism & Hospitality" : "filter-tourism"
}

def build_connector_filters(all_connectors):
    for connector in all_connectors:
        connector['professional_category_filters'] = []
        for category in connector['professional_category']:
            connector['professional_category_filters'].append(data_filters[category])
    return all_connectors

@app.route('/search')
def search():
    return redirect(url_for(connectors))

@app.route('/connectors')
def connectors():
    # ensure logged in
    if not session.get('email', None):
        return redirect("/login?error=notSignedIn&next=connections")
    # retrieve all connectors and pass to template
    all_connectors = build_connector_filters(get_all_connectors())
    return render_template("connectors.html", connectors=all_connectors)

@app.route('/connectors/<connector_id>')
def connector_by_id(connector_id):
    current_connector = get_connector_by_id(connector_id)
    return connector_profile(current_connector['id'], current_connector['last_name'], current_connector['first_name'])

@app.route('/connectors/<connector_id>/<last_name>/<first_name>')
def connector_profile(connector_id, last_name, first_name):
    currentConnector = get_connector_by_id(connector_by_id)
    return render_template("connector.html", connector=currentConnector) 

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)