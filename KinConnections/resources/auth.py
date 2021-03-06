from datetime import datetime, timedelta
from os import error

from flask import (Blueprint, Response, redirect, render_template, request,
                   session, url_for)
from flask_restful import Resource

from .db_wrapper import db_wrapper

auth = Blueprint('auth', __name__)


class Login(Resource):
    error = None
    success = None
    next = None

    def get(self):
        self.error = request.args.get('error')
        return Response(render_template('login.html', error=self.error), mimetype="text/html")

    def post(self):
        self.next = request.args.get('next')

        email = request.form.get('inputEmail').lower()
        password = request.form.get('inputPassword')
        user = db_wrapper.login_auth(email, password)

        if user:
            for key in user['fields'].keys():
                session[key] = user['fields'][key]
        else:
            self.error = "Account not found."

        return redirect('/' + self.next) if self.next else redirect(url_for('home', error=self.error))


class Logout(Resource):
    def get(self):
        session.clear()
        return redirect(url_for('index'))


class Signup(Resource):
    error = None
    success = None

    def get(self):
        if session.get('email', None):
            return render_template("home.html")
        else:
            return Response(render_template('signup.html', type=None, error=self.error, success=self.success), mimetype="text/html")


class SignupConnectee(Resource):
    error = None
    success = None

    def get(self):
        if (session.get('email', None)):
            return redirect(url_for('home'))

        return Response(render_template('signup.html', type="Connectee", error=self.error, success=self.success), mimetype="text/html")

    def post(self):
        if not request.form.get('input_acknowledgement'):
            self.error = "You must agree to abide by the Code of Conduct"
            return Response(render_template('signup.html', type="Connectee", error=self.error, success=self.success), mimetype="text/html")

        self.error = self.__verify_age(request.form.get('input_dob'))
        if self.error:
            return Response(render_template('signup.html', type="Connectee", error=self.error, success=self.success), mimetype="text/html")

        if db_wrapper.login_get_user_info(request.form.get('input_email').lower()):
            self.error = "User with email " + \
                request.form.get('input_email') + " already exists"
        if self.error:
            return Response(render_template('signup.html', type="Connectee", error=self.error, success=self.success), mimetype="text/html")

        form_entries = {}
        form_entries['email'] = request.form.get('input_email').lower()
        form_entries['password'] = request.form.get('input_password')
        form_entries['first_name'] = request.form.get('input_first_name')
        form_entries['last_name'] = request.form.get('input_last_name')
        form_entries['dob'] = request.form.get('input_dob')
        form_entries['region_current'] = request.form.get(
            'input_region_current')
        form_entries['gender'] = request.form.get('input_gender')
        form_entries['languages'] = request.form.getlist('language')
        form_entries['attended_ge'] = bool(request.form.get('attended_ge'))
        form_entries['ge_camps'] = request.form.get('input_ge_camp')
        form_entries['is_ismaili'] = bool(request.form.get('input_is_ismaili'))

        user = db_wrapper.signup_new_connectee(form_entries)

        if not user:
            self.error = "Error creating user"
        else:
            self.success = "New user created"

        return Response(render_template('signup.html', type="Connectee", error=self.error, success=self.success), mimetype="text/html")

    def __verify_age(self, dob_string):
        today_dt = datetime.today()
        dob_dt = datetime.strptime(dob_string, "%Y-%m-%d")
        age = (today_dt - dob_dt) / timedelta(days=365.2425)
        if age < 18:
            return "You must be 18 years of age to use KinConnections"
        return None
