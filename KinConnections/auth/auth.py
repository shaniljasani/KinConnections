import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

auth_bp = Blueprint('auth_bp', __name__)

# signup - ask user type
@auth_bp.route('/signup')
def signup_main():
    return render_template('signup.html', type=None, error=None, success=None)

# signup - connectee
@auth_bp.route('/signup/connectee', methods=('GET', 'POST'))
def signup_connectee():
    # user already logged in
    if (session.get('email', None)):
        return redirect(url_for('home'))
    
    # continue with signup process
    error = None
    success = None
    if request.method == 'POST':
        # get fields
        password = request.form.get('input_password')
        firstName = request.form.get('input_firstName')
        lastName = request.form.get('input_lastNname')
        email = request.form.get('input_email')
        dob = request.form.get('input_dob')
        nationality = request.form.get('input_nationality')
        region_current = request.form.get('input_region_current')
        location_current = request.form.get('input_location_current')
        gender = request.form.get('input_gender')
        english = request.form.get('english')
        french = request.form.get('french')
        spanish = request.form.get('spanish')
        portuguese = request.form.get('portuguese')
        russian = request.form.get('russian')
        tajiki = request.form.get('tajiki')
        farsi = request.form.get('farsi')
        dari = request.form.get('dari')
        urduHindi = request.form.get('urduHindi')
        gujarati = request.form.get('gujarati')
        kutchi = request.form.get('kutchi')
        arabic = request.form.get('arabic')
        is_ismaili = request.form.get('input_is_ismaili')

        return render_template('signup.html', type="Connectee", error=error, success=success)    
        
    return render_template('signup.html', type="Connectee", error=error, success=success)


# signup - connector
@auth_bp.route('/signup/connector', methods=('GET', 'POST'))
def signup_connector():
    # user already logged in
    if (session.get('email', None)):
        return redirect(url_for('home'))
    
    # continue with signup process
    error = None
    success = None
    if request.method == 'POST':
        # get fields
        password = request.form.get('input_password')
        firstName = request.form.get('input_firstName')
        lastName = request.form.get('input_lastNname')
        email = request.form.get('input_email')
        dob = request.form.get('input_dob')
        nationality = request.form.get('input_nationality')
        region_current = request.form.get('input_region_current')
        location_current = request.form.get('input_location_current')
        gender = request.form.get('input_gender')
        english = request.form.get('english')
        french = request.form.get('french')
        spanish = request.form.get('spanish')
        portuguese = request.form.get('portuguese')
        russian = request.form.get('russian')
        tajiki = request.form.get('tajiki')
        farsi = request.form.get('farsi')
        dari = request.form.get('dari')
        urduHindi = request.form.get('urduHindi')
        gujarati = request.form.get('gujarati')
        kutchi = request.form.get('kutchi')
        arabic = request.form.get('arabic')
        title = request.form.get('input_title')
        artsmedia = request.form.get('artsmedia')
        business = request.form.get('business')
        engineering = request.form.get('engineering')
        archgitecture = request.form.get('architecture')
        healthmedicine = request.form.get('healthmedicine')
        humanresources = request.form.get('humenresources')
        internationrelations = request.form.get('internationrelations')
        marketingsales = request.form.get('marketingsales')
        nonprofit = request.form.get('nonprofit')
        tourismhospitality = request.form.get('tourismhospitality')
        education = request.form.get('input_education')
        linkedin = request.form.get('input_linkedin')
        bio = request.form.get('input_bio')
        email = request.form.get('accept_email')
        pics = request.form.get('pics')
        training = request.form.get('accept_training')
        acknowledgement = request.form.get('input_acknowledgement')
        return render_template('signup.html', type="Connector", error=error, success=success)    
        
    return render_template('signup.html', type="Connector", error=error, success=success)

#used for logging in a user
@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    # user already logged in
    if (session['username']):
        return redirect(url_for('home'))

    # login process
    error = None
    if request.method == 'POST':
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        
        error = "Account not found OR Password incorrect"

        # TODO Encryption and Authorization
        if((email == 'kc@kc.com') and ((password == 'sjff'))):
            error = None

        # valid username == no error
        if(error == None):
            session['email'] = email
            return redirect(url_for('home'))

    # else return to login page with/without error
    return render_template('login.html', error = error)

#used to logout a user
@auth_bp.route('/logout')
def logout():
    # clear cookie
    session.clear()
    # redirect to homepage
    return redirect(url_for('index'))