import hashlib, json

def sign_certificate(cert, secret):
    payload = json.dumps(cert, sort_keys=True).encode()
    return hashlib.sha256(payload + secret.encode()).hexdigest()
