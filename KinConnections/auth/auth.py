import functools
import sys

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)

sys.path.append("..")
from db.db_wrapper import db_add

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
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')       # TODO Add encryption
        # create object for entry
        user_object = {'email': email, 'password': password}
        # send to db
        db_add(user_object)

        return render_template('signup.html', type="Connector", error=error, success=success)    
        
    return render_template('signup.html', type="Connector", error=error, success=success)

#used for logging in a user
@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    # user already logged in
    if (session.get('email', None)):
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
