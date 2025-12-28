import json
from jsonschema import validate

def verify_certificate(cert, schema):
    validate(instance=cert, schema=schema)
    return 'VERIFIED'
