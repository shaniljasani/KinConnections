# db_wrapper.py - KinConnections
# Serves as wrapper for database access (airtable or otherwise)

import logging
import os
from os.path import dirname, join

import bcrypt
from airtable import Airtable
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

airtable_connectees = Airtable(os.getenv('AIRTABLE_BASE_ID'), 'connectees', os.getenv('AIRTABLE_API_KEY'))
airtable_connectors = Airtable(os.getenv('AIRTABLE_BASE_ID'), 'connectors', os.getenv('AIRTABLE_API_KEY'))
airtable_auth = Airtable(os.getenv('AIRTABLE_BASE_ID'), 'auth', os.getenv('AIRTABLE_API_KEY'))

class db_wrapper:
    # --------------------------------------------------------
    #       AUTH FUNCTIONS
    # --------------------------------------------------------

    def login_auth(email, password):
        matching_users_arr = airtable_connectees.search('email', email)
        if matching_users_arr:
            user = matching_users_arr[0]
            auth_info_arr = airtable_auth.search('user_id', user['fields']['id'])
            if auth_info_arr:
                password_hash = auth_info_arr[0]['fields']['password_hash']
                if(bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))):
                    return user
        return None

    def login_get_user_info(email):
        matching_users = airtable_connectees.search('email', email)
        for user in matching_users:
            return user['fields']
        return None

    # --------------------------------------------------------
    #       REGISTRATION FUNCTIONS
    # --------------------------------------------------------

    def signup_new_connectee(form_entries):
        pw_salt = bcrypt.gensalt()
        pw_hash = bcrypt.hashpw(
            form_entries['password'].encode('utf-8'), 
            pw_salt
        )
        user_id = list()
        form_entries.pop('password')
        
        try:
            user = airtable_connectees.insert(form_entries)
            user_id.append(user['id'])
        except:
            logging.error("There was an issue creating user record in user table")
            return None
        
        try:
            airtable_auth.insert({
                "password_hash": pw_hash.decode('utf-8'),
                "user_id": user_id
            })
        except:
            logging.error("There was an issue creating auth record for user: " + str(user))
            airtable_connectees.delete(user_id.pop())
            return None
    
        return user

    # --------------------------------------------------------
    #       CONNECTIONS FUNCTIONS
    # --------------------------------------------------------

    newDemoProfile = {
            "id": 0,
            "first_name" : "Ali",
            "last_name" : "Kassim Longnasdfsdfsdfsdfs",
            "email" : "ceo@kc.com",
            "password" : "demopass",
            "dob" : "37257",
            "country_origin" : "United States",
            "region_current" : "United States",
            "location_current" : "Bay Area, CA",
            "gender" : "male",
            "languages" : ["English", "Hindi/Urdu"],
            "acknowledgement" : "TRUE",
            "user_type" : "Connector",

            "title" : "CEO of OneCompany | Educator | Teacher | Strategist",
            "professional_category" : ["Business", "Engineering"],
            "education" : {"School0Name" : "UT Austin", "School0Major" : "ECE"},
            "linkedin" : "https://linkedin.com/in/kabir",
            "bio" : "Kabir is the Founder, President, and CEO of OneTrust. In under five years, Kabir has grown the company into the #1 fastest growing company on the Inc. 500 and category-defining enterprise technology platform to operationalize trust. According to TCV, OneTrust is the fastest growing enterprise software company in history. OneTrust has largely pioneered the trust technology market, has been awarded 150 patents, and acquired 7 companies along the way.",
            "images" : ["/static/img/users/shanil.jpg"],
            "approved" : "TRUE",
        }
    newDemoProfile1 = {
            "id": 0,
            "first_name" : "Ali",
            "last_name" : "Kassim Longnasdfsdfsdfsdfs",
            "email" : "ceo@kc.com",
            "password" : "demopass",
            "dob" : "37257",
            "country_origin" : "United States",
            "region_current" : "United States",
            "location_current" : "Bay Area, CA",
            "gender" : "male",
            "languages" : ["English", "Hindi/Urdu"],
            "acknowledgement" : "TRUE",
            "user_type" : "Connector",

            "title" : "CEO of OneCompany | Educator | Teacher | Strategist",
            "professional_category" : ["Arts & Media", "Engineering"],
            "education" : {"School0Name" : "UT Austin", "School0Major" : "ECE"},
            "linkedin" : "https://linkedin.com/in/kabir",
            "bio" : "Kabir is the Founder, President, and CEO of OneTrust. In under five years, Kabir has grown the company into the #1 fastest growing company on the Inc. 500 and category-defining enterprise technology platform to operationalize trust. According to TCV, OneTrust is the fastest growing enterprise software company in history. OneTrust has largely pioneered the trust technology market, has been awarded 150 patents, and acquired 7 companies along the way.",
            "images" : ["/static/img/users/shanil.jpg"],
            "approved" : "TRUE",
        }

    def get_all_connectors():
        all =  [ connector['fields'] for connector in airtable_connectors.get_all() ]
        all_approved = []
        for connector in all:
            if(connector.get('approved', None)):
                all_approved.append(connector)
        return all_approved

    def get_connector_by_id(id):
        if airtable_connectors.search('id', id):
            return airtable_connectors.search('id', id)[0]['fields']
        return None
