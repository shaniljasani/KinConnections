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
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')
        
        error = "yes"

        if((username == 'kc') and ((password == 'sjff'))):
            error = None

        if(error == None):
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html', error = error)

#used to logout a user [clears cookies]
@auth_bp.route('/logout')
def logout():
    session.clear()
    # redirect to homepage
    return redirect(url_for('index'))