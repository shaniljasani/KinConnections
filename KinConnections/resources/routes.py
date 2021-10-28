from .auth import Login, Logout, Signup, SignupConnectee
from .connector import Connector, ConnectorExternalApi, Connectors


def initialize_routes(api):
 api.add_resource(Login, '/login')
 api.add_resource(Logout, '/logout')
 api.add_resource(Signup, '/signup')
 api.add_resource(SignupConnectee, '/signup/connectee')
 api.add_resource(Connectors, '/connectors')
 api.add_resource(Connector, '/connector/<id>')
 api.add_resource(ConnectorExternalApi, '/api/external/connector')
