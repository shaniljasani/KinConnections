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

def get_all_connectors():
    all =  [ connector['fields'] for connector in airtable_connectors.get_all() ]
    all_approved = []
    for connector in all:
        if(connector.get('approved', None)):
            connector["education"] = ""
            all_approved.append(connector)
    return all_approved
    
# TODO this could be improved
def get_connector_by_name(name):
    return airtable_connectors.search('full_name', name)

def get_connector_by_id(id):
    if airtable_connectors.search('id', id):
        return airtable_connectors.search('id', id)[0]['fields']
    return None