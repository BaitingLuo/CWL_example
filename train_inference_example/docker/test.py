from joblib import load
import pandas as pd
import sys
# Load the model
model_filename = sys.argv[2]
loaded_rf = load(model_filename)

file_path = sys.argv[1]

# Simulate reading the CSV file
df = pd.read_csv(file_path, header=0)
features = df.iloc[:, :4]  # assuming the first four columns are features
predictions = loaded_rf.predict(features)
print("Predictions:", predictions)
from sklearn.metrics import accuracy_score

true_species = df['species'].to_numpy()  # Actual species
accuracy = accuracy_score(true_species, predictions)
with open("output.txt", "w") as f:
    # Write predictions
    f.write("Predictions:\n")
    for i, pred in enumerate(predictions):
        f.write(f"Sample {i}: Predicted species = {pred}\n")

    # Write accuracy
    f.write(f"\nAccuracy: {accuracy:.3f}")