import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from datetime import datetime

# Load the trained model
model = load_model("/Users/thetanmaymishra/Desktop/vlsi_ml/models/classifier.h5")

# Load test patterns (new test data)
test_data_path = "/Users/thetanmaymishra/Desktop/vlsi_ml/data/test_patterns.csv"

if not os.path.exists(test_data_path):
    raise FileNotFoundError("Test patterns CSV file not found!")

X_test = pd.read_csv(test_data_path, header=None).values

# Make predictions
predictions = model.predict(X_test)

# Convert probabilities to binary labels (0 or 1)
binary_predictions = (predictions >= 0.5).astype(int)

# Ensure the results directory exists before saving
results_dir = "/Users/thetanmaymishra/Desktop/vlsi_ml/results"
os.makedirs(results_dir, exist_ok=True)  # Creates directory if it doesn’t exist

# Define the CSV file where results will be stored
output_file = os.path.join(results_dir, "test_results.csv")

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create DataFrame with Timestamp and Predictions
results_df = pd.DataFrame({
    "Timestamp": [timestamp] * len(binary_predictions),  # Add timestamp to each row
    "Prediction": binary_predictions.flatten()  # Convert to 1D array
})

# Append to CSV (Create if doesn't exist)
if not os.path.exists(output_file):
    results_df.to_csv(output_file, index=False)  # Create new file with headers
else:
    results_df.to_csv(output_file, mode="a", header=False, index=False)  # Append new data

print(f"Predictions appended to {output_file}")
