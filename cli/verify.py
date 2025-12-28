import sys, json
from verification.verify_certificate import verify_certificate

with open(sys.argv[1]) as f:
    cert = json.load(f)

result = verify_certificate(cert)
print(result)
