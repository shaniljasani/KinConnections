from resources.connector import (Connector, ConnectorExternalApi, Connectors,
                                 ConnectorsApi)

from .auth import Login, Logout, Signup, SignupConnectee
from .email_wrapper import Email


def initialize_routes(api):
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
    api.add_resource(Signup, '/signup')
    api.add_resource(SignupConnectee, '/signup/connectee')
    api.add_resource(Connectors, '/connectors')
    api.add_resource(Connector, '/connector/<id>')

    api.add_resource(ConnectorsApi, '/api/connectors')
    api.add_resource(Email, '/api/send_email/<id>')

    api.add_resource(ConnectorExternalApi, '/api/external/connector')
