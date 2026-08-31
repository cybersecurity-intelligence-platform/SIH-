import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample criminal investigation text
text = """
Rahul Patil met Amit Sharma in Pune.
Sneha Joshi reported the case to Pune Police.
The investigation found CCTV evidence near Pune.
"""

# Process text
doc = nlp(text)

print("\n=== NAMED ENTITY RECOGNITION ===\n")

for ent in doc.ents:
    print(f"Entity: {ent.text}")
    print(f"Type  : {ent.label_}")
    print(f"Meaning: {spacy.explain(ent.label_)}")
    print("-" * 40)