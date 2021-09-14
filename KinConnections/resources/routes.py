from resources.connector import Connector, Connectors
from .auth import Login, Logout, Signup, SignupConnectee

def initialize_routes(api):
 api.add_resource(Login, '/login')
 api.add_resource(Logout, '/logout')
 api.add_resource(Signup, '/signup')
 api.add_resource(SignupConnectee, '/signup/connectee')
 api.add_resource(Connectors, '/connectors')
 api.add_resource(Connector, '/connector/<id>')