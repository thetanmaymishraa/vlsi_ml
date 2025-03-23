import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import pandas as pd
import os
from datetime import datetime  # Import datetime module

# Load dataset
data_path = "/Users/thetanmaymishra/Desktop/vlsi_ml/data/test_patterns.csv"
labels_path = "/Users/thetanmaymishra/Desktop/vlsi_ml/data/labels.csv"

if not os.path.exists(data_path) or not os.path.exists(labels_path):
    raise FileNotFoundError("Test patterns or labels CSV file not found!")

X = pd.read_csv(data_path, header=None).values
y = pd.read_csv(labels_path, header=None).values

# Define a simple neural network classifier
classifier = Sequential([
    Dense(4, activation='relu', input_shape=(X.shape[1],)),  # Hidden layer with 4 neurons
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the classifier
classifier.fit(X, y, epochs=100, batch_size=4, shuffle=True, verbose=1)

# Save the trained model
model_dir = "/Users/thetanmaymishra/Desktop/vlsi_ml/models"
os.makedirs(model_dir, exist_ok=True)  # Ensure the directory exists
classifier.save(os.path.join(model_dir, "classifier.h5"))

# Evaluate the model
loss, accuracy = classifier.evaluate(X, y)

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS

# Define report filename with timestamp
report_dir = "/Users/thetanmaymishra/Desktop/vlsi_ml/results"
os.makedirs(report_dir, exist_ok=True)  # Ensure the directory exists
report_path = os.path.join(report_dir, f"evaluation_report_{timestamp}.txt")

# Save evaluation results
with open(report_path, "w") as f:
    f.write(f'Timestamp: {timestamp}\n')
    f.write(f'Fault Detection Model Accuracy: {accuracy * 100:.2f}%\n')

print(f'Report saved: {report_path}')
print(f'Fault Detection Model Accuracy: {accuracy * 100:.2f}%')
