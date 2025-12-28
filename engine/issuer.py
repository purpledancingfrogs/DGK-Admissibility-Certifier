import json, hashlib, datetime
from crypto.sign import sign_certificate

def issue_certificate(trace, invariants_hash, kts_state, secret):
    trace_hash = hashlib.sha256(json.dumps(trace, sort_keys=True).encode()).hexdigest()
    cert = {
        "certificate_id": f"DGK-{trace_hash[:12]}",
        "issued_at": datetime.datetime.utcnow().isoformat() + "Z",
        "invariants_hash": invariants_hash,
        "trace_hash": trace_hash,
        "kappa_tau_sigma_state": kts_state,
        "admissibility_status": "ADMISSIBLE",
    }
    cert["signature"] = sign_certificate(cert, secret)
    return cert
