# VLSI Fault Detection Using Machine Learning

## 📌 Overview
This project implements a **Machine Learning (ML) model** to detect **stuck-at faults** in digital **VLSI circuits**. The model uses:
- **Deep Sparse Autoencoder** for feature extraction.
- **Binary Classifier** for fault detection.
- **Test patterns** generated from ATPG tools or simulations.

## 📂 Folder Structure
```
vlsi_ml/
│── data/                    # Input test patterns & labels
│   ├── test_patterns.csv    # Test patterns (circuit data)
│   ├── labels.csv           # Fault labels (0 = No Fault, 1 = Fault)
│── models/                  # Trained models
│   ├── autoencoder.h5       # Autoencoder for feature extraction
│   ├── classifier.h5        # Binary classifier for fault detection
│── scripts/                 # Training & testing scripts
│   ├── train_model.py       # Train the model
│   ├── test_model.py        # Test the trained model
│── results/                 # Evaluation results
│   ├── evaluation_report.txt
│── requirements.txt         # Required Python libraries
│── README.md                # Project documentation
```

## 🔹 1. Install Dependencies
Run the following command to install the required Python libraries:
```bash
pip install -r requirements.txt
```

## 🔹 2. Prepare Input Data
You need **two CSV files** inside `data/`:

### `test_patterns.csv` (Circuit Input Data)
Each row represents a test pattern in binary format:
```
1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1
0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0
...
```

### `labels.csv` (Fault Labels)
Each row corresponds to a fault label (`0` = No Fault, `1` = Fault):
```
1
0
1
0
...
```

## 🔹 3. Generate Test Patterns
Test patterns can be generated using:
1. **ATALANTA ATPG Tool**:
   ```bash
   atalanta -t test_patterns.txt circuit.bench
   ```
   Convert the output into `test_patterns.csv`.
2. **Logic Simulators** (Cadence, Synopsys, Xilinx Vivado): Simulate your circuit and save the binary input patterns.
3. **Manual Entry** (For small circuits).

## 🔹 4. Train the Models
Run the training script to train the **Autoencoder** and **Binary Classifier**:
```bash
cd scripts
python train_model.py
```
✅ This saves trained models inside `models/`.

## 🔹 5. Test the Models
Use the trained models to detect faults in new test patterns:
```bash
python test_model.py
```
✅ Predictions will be saved in `results/predictions.csv`.

## 📊 Results
After training, model accuracy will be saved in `results/evaluation_report.txt`.

## 🚀 Next Steps
- Improve model accuracy with **real circuit data**.
- Add support for **other fault types** (bridging, delay faults).
- Integrate with **hardware testing environments**.

---

## 📞 Need Help?
For any questions, feel free to reach out!

