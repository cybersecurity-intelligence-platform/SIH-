from transformers import pipeline

print("Loading AI model...")

# Sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

text = """
The investigation found important evidence related to the
criminal case. The information requires further investigation.
"""

result = classifier(text)

print("\n=== TRANSFORMERS NLP ===")
print("Text:", text.strip())
print("Result:", result)