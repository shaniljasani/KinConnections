# db_wrapper.py - KinConnections
# Serves as wrapper for database access (airtable or otherwise)

import os
from airtable import Airtable
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

airtable_connectees = Airtable(os.getenv('AIRTABLE_BASE_ID'), 'connectees', os.getenv('AIRTABLE_API_KEY'))
airtable_connectors = Airtable(os.getenv('AIRTABLE_BASE_ID'), 'connectors', os.getenv('AIRTABLE_API_KEY'))

# --------------------------------------------------------
#       AUTH FUNCTIONS
# --------------------------------------------------------

def login_auth(email, password):
    matching_users = airtable_connectees.search('email', email)
    for user in matching_users:
        if(user['fields']['password'] == password):
        # password match
            return None
        # else incorrect
        else:
            return "Incorrect password"
    return "Account not found"

def login_get_user_info(email):
    matching_users = airtable_connectees.search('email', email)
    for user in matching_users:
        return user['fields']
    return None

# --------------------------------------------------------
#       REGISTRATION FUNCTIONS
# --------------------------------------------------------

def verify_age(dob_string):
    today_dt = datetime.today()
    dob_dt = datetime.strptime(dob_string, "%Y-%m-%d")
    age = (today_dt - dob_dt) / timedelta(days=365.2425)
    if age < 18:
        return "You must be 18 years of age to use KinConnections"
    return None

def signup_new_connectee(form_entries):
    success = None
    error = None
    # duplicate email check
    if airtable_connectees.search('email', form_entries['email']):
        error = "User with email " + form_entries['email'] + " already exists"
        return success, error
    # 18+ check
    error = verify_age(form_entries['dob'])
    airtable_connectees.insert(form_entries)
    success = "New User Created"
    return success, error

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
    
# TODO this could be improved
def get_connector_by_name(name):
    return airtable_connectors.search('full_name', name)

def get_connector_by_id(id):
    if airtable_connectors.search('id', id):
        return airtable_connectors.search('id', id)[0]['fields']
    return None