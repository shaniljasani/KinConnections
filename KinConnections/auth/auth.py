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
        return render_template('signup.html', type="Connector", error=error, success=success)    
        
    return render_template('signup.html', type="Connector", error=error, success=success)

#used for logging in a user
@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    # init error to None
    error = None

    # if follow path is different once logged in
    next = request.args.get('next')
    print(next)

    # if you're sent from another page
    error = request.args.get('error')
    if error == 'notSignedIn':
        error = "You must be signed in to view this page"

    # user already logged in
    if (session.get('email', None)):
        if next:
            return redirect('/'+next)
        return redirect(url_for('home'))

    # login process
    
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
            if next:
                return redirect('/' + next )
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