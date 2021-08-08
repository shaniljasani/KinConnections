# db_wrapper.py - KinConnections
# Serves as wrapper for database access (airtable or otherwise)

# --------------------------------------------------------
#       AUTH FUNCTIONS
# --------------------------------------------------------

def login_auth(email, password):
    if ((email == 'kc@kc.com') and (password == 'sjff')):
        return None
    else:
        return "account not found or password incorrect"

def login_get_user_info(email):
    user = {}
    user['email'] = email
    user['name'] = 'Shanil'
    return user

# --------------------------------------------------------
#       REGISTRATION FUNCTIONS
# --------------------------------------------------------

def signup_new_connectee(form_entries):
    success = "New User Created"
    error = "User with email " + form_entries['email'] + " already exists"

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
    return [newDemoProfile,newDemoProfile1,newDemoProfile]

def get_connector_by_name(name):
    return newDemoProfile

def get_connector_by_id(id):
    return newDemoProfile