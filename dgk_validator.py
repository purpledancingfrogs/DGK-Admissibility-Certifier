# -*- coding: utf-8 -*-
"""
DGK Provenance & Admissibility Validator

Rejects any output that lacks:
- source provenance
- timestamp
- reproducibility marker
- invariant hash
"""

import time
import hashlib
import json

REQUIRED_FIELDS = [
    "content",
    "sources",
    "timestamp",
    "reproducible",
    "invariant_hash"
]

class DGKRejection(Exception):
    pass


def validate(payload: dict) -> None:
    missing = [f for f in REQUIRED_FIELDS if f not in payload]
    if missing:
        raise DGKRejection(f"Missing required fields: {missing}")

    if not payload["sources"]:
        raise DGKRejection("No provenance sources provided")

    if payload["reproducible"] is not True:
        raise DGKRejection("Output not marked reproducible")

    expected = hashlib.sha256(
        json.dumps(payload["content"], sort_keys=True).encode("utf-8")
    ).hexdigest()

    if payload["invariant_hash"] != expected:
        raise DGKRejection("Invariant hash mismatch")


def admissible(payload: dict) -> bool:
    try:
        validate(payload)
        return True
    except DGKRejection:
        return False