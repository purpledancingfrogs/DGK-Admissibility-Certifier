def gate_llm_output(output):
    return {
        "raw_output": output,
        "status": "NON_ADMISSIBLE",
        "reason": "Unbound probabilistic generation"
    }
