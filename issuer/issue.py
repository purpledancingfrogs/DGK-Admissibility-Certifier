import uuid, datetime, json
from crypto.sign import sign_certificate

def issue_certificate(trace_hash, invariants_hash, kts_state, secret):
    cert = {
        "certificate_id": str(uuid.uuid4()),
        "issued_at": datetime.datetime.utcnow().isoformat() + "Z",
        "trace_hash": trace_hash,
        "invariants_hash": invariants_hash,
        "kappa_tau_sigma_state": kts_state,
        "admissibility_status": "ADMISSIBLE"
    }
    cert["signature"] = sign_certificate(cert, secret)
    return cert
