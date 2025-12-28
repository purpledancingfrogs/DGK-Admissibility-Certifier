## Verification Instructions

1. Validate certificate against schema:
   python verification/verify_certificate.py

2. Recompute trace hash:
   sha256sum examples/demo_trace.json

3. Compare invariants hash:
   cat INVARIANTS.md | sha256sum

4. Confirm κ–τ–Σ bounds preserved.

If all checks pass, the decision is ADMISSIBLE.
