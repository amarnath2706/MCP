import re

def extract_symptoms(text: str) -> list[str]:
    # Very basic extraction
    symptoms = re.findall(r"\b(headache|fever|nausea|fatigue|pain)\b", text.lower())
    return list(set(symptoms))