import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

auth_bp = Blueprint('auth_bp', __name__)

#used for registering a user
@auth_bp.route('/signup', methods=('GET', 'POST'))
def signup():
    error = None
    if request.method == 'POST':
        username = request.form.get('inputUsername')
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        return redirect(url_for('auth_bp.login'))            
        
    return render_template('signup.html')

#used for logging in a user
@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
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