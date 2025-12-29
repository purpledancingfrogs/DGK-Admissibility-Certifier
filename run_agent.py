# -*- coding: utf-8 -*-
"""
AUREON Laptop Agent Runner
All outputs MUST pass DGK admissibility.
"""

import time
import json
import hashlib
from dgk_validator import admissible, DGKRejection


def produce_payload(content, sources):
    timestamp = int(time.time())
    invariant_hash = hashlib.sha256(
        json.dumps(content, sort_keys=True).encode("utf-8")
    ).hexdigest()

    return {
        "content": content,
        "sources": sources,
        "timestamp": timestamp,
        "reproducible": True,
        "invariant_hash": invariant_hash,
    }


def emit(content, sources):
    payload = produce_payload(content, sources)

    if not admissible(payload):
        raise DGKRejection("Output rejected by DGK")

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    # Example admissible output
    emit(
        content={"message": "AUREON agent online"},
        sources=["internal_bootstrap"]
    )