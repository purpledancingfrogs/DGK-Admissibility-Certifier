# AUREON Laptop Agent — DGK Admissibility Reference

This repository demonstrates a **deterministic, admissibility-gated intelligence runtime**.

## What this is
AUREON / ASIOS is not a chatbot.
All outputs are rejected unless they satisfy **DGK admissibility invariants**.

## DGK invariants enforced
Every emitted payload MUST include:
- content
- source provenance (non-empty)
- timestamp
- reproducibility flag
- invariant hash (SHA-256 of content)

If any invariant is missing or inconsistent, output **hard-fails**.

## Files
- `run_agent.py` — enforced output runner (no bypass path)
- `dgk_validator.py` — admissibility gate

## Run

Any hallucinated, unverifiable, or source-less output is structurally impossible.

This is a **public reference implementation** of admissible intelligence execution.