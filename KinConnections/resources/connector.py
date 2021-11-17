import json

from flask import (Blueprint, Response, redirect, render_template, request,
                   session, url_for)
from flask_restful import Resource

from .db_wrapper import db_wrapper
from .models import ConnectorExternalApiSchema

connector_external_api_schema = ConnectorExternalApiSchema()


class Connectors(Resource):
    def get(self):
        if not session.get('email', None):
            return redirect("/login?error=notSignedIn&next=connections")

        all_connectors = db_wrapper.get_all_connectors()
        return Response(render_template("connectors.html", connectors=all_connectors), mimetype="text/html")


class ConnectorsApi(Resource):
    def get(self):
        if not session.get('email', None):
            return 'Unauthorized Access', 401

        all_connectors = json.dumps(db_wrapper.get_all_connectors())
        return Response(all_connectors, mimetype="application/json", status=200)


class Connector(Resource):
    def get(self, id):
        connector = db_wrapper.get_connector_by_id(id)
        return Response(render_template("connector.html", connector=connector), mimetype="text/html")

class ConnectorExternalApi(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
           return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data = connector_external_api_schema.load(json_data)
        user = db_wrapper.add_connector(data)
        if not user:
            return {"message": "Error adding user to KinConnections"}, 500
        return user
