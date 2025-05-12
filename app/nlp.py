# app/nlp.py

from transformers import pipeline
import re

# Initialize the NER pipeline with a lighter model
ner = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def extract_aadhar_data(text):
    """
    Extracts Aadhaar-related information from the provided text.
    """
    data = {
        "name": None,
        "dob": None,
        "gender": None,
        "aadhar_number": None
    }

    # Extract Aadhaar number using regex
    match = re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', text)
    if match:
        data["aadhar_number"] = match.group()

    # Extract DOB using regex
    match = re.search(r'\b\d{2}/\d{2}/\d{4}\b', text)
    if match:
        data["dob"] = match.group()

    # Extract gender
    if re.search(r'\bMale\b', text, re.IGNORECASE):
        data["gender"] = "Male"
    elif re.search(r'\bFemale\b', text, re.IGNORECASE):
        data["gender"] = "Female"

    # Use NER to extract name
    ner_results = ner(text)
    for entity in ner_results:
        if entity['entity_group'] == 'PER':
            data["name"] = entity['word']
            break

    return data
