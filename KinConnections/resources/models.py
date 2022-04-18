from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, pre_load, validate

ma = Marshmallow()

# {	
# 	"first_name" : "Fahim",
# 	"last_name" : "Karim",
# 	"email" : "fahimkarim@gmail.com",
# 	"dob" : "2021-08-02",
# 	"country_origin" : "United States of America",
# 	"region_current" : "United States of America",
# 	"gender" : "Male",
# 	"languages" : ["English"]
# }
class ConnectorExternalApiSchema(ma.Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    dob = fields.String(required=True)
    country_origin = fields.String(required=True)
    region_current = fields.String(required=True)
    gender = fields.String(required=True)
    languages = fields.List(fields.String, required=True)
