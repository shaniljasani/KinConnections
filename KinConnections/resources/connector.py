from flask import Blueprint, Response, request, render_template, session, redirect, url_for
from flask_restful import Resource
from .db_wrapper import db_wrapper

class Connectors(Resource):
    def get(self):
        if not session.get('email', None):
            return redirect("/login?error=notSignedIn&next=connections")
        
        all_connectors = build_connector_filters(db_wrapper.get_all_connectors())
        return Response(render_template("connectors.html", connectors=all_connectors), mimetype="text/html")

class Connector(Resource):
    def get(self, id):
        connector = db_wrapper.get_connector_by_id(id)
        return Response(render_template("connector.html", connector=connector), mimetype="text/html")

data_filters = {
    "Arts & Media" : "filter-artsmedia",
    "Business" : "filter-business",
    "Engineering" : "filter-engineering",
    "Architecture" : "filter-architecture",
    "Health & Medicine" : "filter-healthmedicine",
    "Human Resources" : "filter-humanresources",
    "International Relations, Law & Policy" : "filter-irlp",
    "Marketing & Sales" : "filter-marketingsales",
    "Non-Profit & Foundation" : "filter-nonprofit",
    "Tourism & Hospitality" : "filter-tourism",

    "Arabic" : "filter-Arabic",
    "Dari" : "filter-Dari",
    "English" : "filter-English",
    "Farsi" : "filter-Farsi",
    "French" : "filter-French",
    "Gujarati" : "filter-Gujarati",
    "Kutchi" : "filter-Kutchi",
    "Portuguese" : "filter-Portuguese",
    "Russian" : "filter-Russian",
    "Spanish" : "filter-Spanish",
    "Urdu/Hindi" : "filter-Urduhindi"
}

def build_connector_filters(all_connectors):
    for connector in all_connectors:
        connector['professional_category_filters'] = []
        connector['language_category_filters'] = []
        for category in connector['professional_category']:
            connector['professional_category_filters'].append(data_filters[category])
        for language in connector['languages']:
            connector['language_category_filters'].append(data_filters[language])
    return all_connectors