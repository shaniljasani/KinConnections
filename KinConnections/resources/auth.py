from flask import Blueprint, Response, request, render_template, session, redirect, url_for
from flask_restful import Resource
from .db_wrapper import login_auth, login_get_user_info, signup_new_connectee

auth = Blueprint('auth', __name__)

class Login(Resource):
    def get(self):
        return Response(render_template('login.html'),  mimetype="text/html")

    def post(self):
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        
        next = request.args.get('next')

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

class Logout(Resource):
    def get(self):
        session.clear()
        return redirect(url_for('index'))

class Signup(Resource):
    def get(self):
        if session.get('email', None):
            return render_template("home.html")
        else:
            return Response(render_template('signup.html', type=None, error=None, success=None), mimetype="text/html")

class SignupConnectee(Resource):
    def get(self):
        if (session.get('email', None)):
            return redirect(url_for('home'))
        
        error = None
        success = None
        return Response(render_template('signup.html', type="Connectee", error=error, success=success), mimetype="text/html")
    
    def post(self):
        if not (request.form.get('input_acknowledgement', None)):
            error = "You must agree to abide by the Code of Conduct"
            success=None
            return render_template('signup.html', type="Connectee", error=error, success=success)
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
