SYMBOL_DB = {
    "water": "Symbolizes deep unconscious thoughts (Freud).",
    "snake": "Represents primal instincts or transformation (Jung).",
    "teeth": "Fear of change or aging (Freud).",
    "falling": "Loss of control or anxiety (Freud).",
    "mother": "Anima archetype, nurturing force (Jung).",
    "mirror": "Self-reflection and persona (Jung)."
}

def interpret_dream(text):
    found = [symbol for symbol in SYMBOL_DB if symbol in text.lower()]
    if found:
        return " | ".join([f"{symbol}: {SYMBOL_DB[symbol]}" for symbol in found])
    return "Could not match known symbols. Consider elaborating your dream."
