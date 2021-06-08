
from flask import Blueprint, redirect, render_template, request, session

connections_bp = Blueprint('connections_bp', __name__)


newDemoProfile = {
    "first_name" : "Ali Muhammad",
    "last_name" : "Joint-LastName",
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

    "title" : "CEO of OneTrust | Educator | Teacher | Strategist",
    "professional_category" : ["Business", "Technology"],
    "education" : {"School0Name" : "UT Austin", "School0Major" : "ECE"},
    "linkedin" : "https://linkedin.com/in/kabir",
    "bio" : "Kabir is the Founder, President, and CEO of OneTrust. In under five years, Kabir has grown the company into the #1 fastest growing company on the Inc. 500 and category-defining enterprise technology platform to operationalize trust. According to TCV, OneTrust is the fastest growing enterprise software company in history. OneTrust has largely pioneered the trust technology market, has been awarded 150 patents, and acquired 7 companies along the way.",
    "images" : ["/static/img/users/shanil.jpg"],
    "approved" : "TRUE",
}


newDemoProfile = {
    "first_name" : "Ali Muhammad",
    "last_name" : "Joint-LastName",
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

    "title" : "CEO of OneTrust | Educator | Teacher | Strategist",
    "professional_category" : ["Business", "Technology"],
    "education" : {"School0Name" : "UT Austin", "School0Major" : "ECE"},
    "linkedin" : "https://linkedin.com/in/kabir",
    "bio" : "Kabir is the Founder, President, and CEO of OneTrust. In under five years, Kabir has grown the company into the #1 fastest growing company on the Inc. 500 and category-defining enterprise technology platform to operationalize trust. According to TCV, OneTrust is the fastest growing enterprise software company in history. OneTrust has largely pioneered the trust technology market, has been awarded 150 patents, and acquired 7 companies along the way.",
    "images" : ["/static/img/users/shanil.jpg"],
    "approved" : "TRUE"
}


newDemoProfile2 = {
    "first_name" : "Kabir",
    "last_name" : "Barday",
    "email" : "ceo@kc.com",
    "password" : "demopass",
    "dob" : "37257",
    "country_origin" : "USA",
    "region_current" : "USA",
    "location_current" : "Bay Area, CA",
    "gender" : "male",
    "languages" : ["English", "Hindi/Urdu"],
    "acknowledgement" : "TRUE",
    "user_type" : "Connector",

    "title" : "CEO of OneTrust",
    "professional_category" : ["Business", "Technology"],
    "education" : {"School0Name" : "UT Austin", "School0Major" : "ECE"},
    "linkedin" : "https://linkedin.com/in/kabir",
    "bio" : "hi my name is pickles",
    "images" : ["/static/img/team-2.jpg", ""],
    "approved" : "TRUE"
}

profiles = [newDemoProfile, newDemoProfile2]


# search endpoint redirect
@connections_bp.route('/search')
def search():
    return redirect('/connectors')

# connector lookup
@connections_bp.route('/connectors')
def connectors():
    # ensure user logged in
    if not (session.get('email', None)):
        return redirect("/login?error=notSignedIn")
    # grab all connectors and pass to template
    # for now all of them
    return render_template('connectors.html', connectors=profiles)


@connections_bp.route('/connectors/<uid>')
def connector_profile_uid(uid):

    try:
        currentConnector = profiles[int(uid)]
    except (IndexError, ValueError) as e:
        currentConnector = None
        return render_template("connector.html", connector=currentConnector)

    redirect_string = "/connectors/" + uid + "/" + currentConnector['last_name'] + "/" + currentConnector['first_name'] 
    return redirect(redirect_string)

@connections_bp.route('/connectors/<uid>/<last_name>/<first_name>')
def connector_profile_uid_ln_fn(uid, last_name, first_name):
    try:
        currentConnector = profiles[int(uid)]
    except IndexError:
        currentConnector = None
    return render_template("connector.html", connector=currentConnector)