from sklearn.ensemble import IsolationForest

# Criminal investigation data
# [number_of_cases, number_of_evidence]
data = [
    [1, 1],
    [1, 1],
    [1, 1],
    [10, 10]
]

# Create anomaly detection model
model = IsolationForest(
    contamination=0.25,
    random_state=42
)

model.fit(data)

# Predict anomalies
predictions = model.predict(data)

print("\n=== SCikit-learn Anomaly Analysis ===\n")

for i, prediction in enumerate(predictions):
    if prediction == -1:
        print(f"Record {i + 1}: ANOMALY DETECTED")
    else:
        print(f"Record {i + 1}: Normal")