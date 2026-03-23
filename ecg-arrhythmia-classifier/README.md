# ECG Arrhythmia Classifier

A production-ready deep learning pipeline designed to classify ECG heartbeats into five clinical categories.
This project bridges the gap between advanced signal processing and clinical reporting, providing an interactive dashboard for medical analysis.

---

## 🚀 Key Features

* **1D-CNN Architecture** – Optimized for spatial morphology detection in ECG signals
* **Real-time Visualization** – Interactive ECG waveform rendering using Streamlit
* **Batch Processing** – Classify thousands of heartbeats in seconds
* **Clinical Reporting** – Automated PDF reports with diagnostic summaries
* **Data Balancing** – SMOTE integration for improved rare-class detection

---

## 📁 Project Structure

```
ecg-arrhythmia-classifier/
│
├── data/                      # Local dataset (download required)
│   ├── mitbih_train.csv
│   └── mitbih_test.csv
│
├── sample-outputs/            # App screenshots
│   ├── single_analysis_1.png
│   ├── single_analysis_2.png
│   ├── batch_processing_1.png
│   └── batch_processing_2.png
│
├── app.py                     # Streamlit dashboard
├── experiments.ipynb          # Model training & experimentation
├── ecg_lstm_model.keras       # Trained model weights
├── scaler.pickle              # Data scaler
├── requirements.txt           # Dependencies
├── CHALLENGES.md              # Engineering retrospective
├── test_samples.csv           # Demo dataset
└── sample_test.csv            # Additional demo file
```

---

## 📊 Dataset: MIT-BIH Arrhythmia

This project uses the **MIT-BIH Arrhythmia Database**, a gold-standard dataset for ECG classification.

### Class Distribution (Original)

| Label | Category             | Count  |
| ----- | -------------------- | ------ |
| 0     | Normal (N)           | 72,471 |
| 1     | Supraventricular (S) | 2,223  |
| 2     | Ventricular (V)      | 5,788  |
| 3     | Fusion (F)           | 641    |
| 4     | Unclassifiable (Q)   | 6,431  |

> ⚠️ SMOTE was applied to address class imbalance and improve sensitivity for rare arrhythmias.

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/deep-learning-signal-processing.git
cd deep-learning-signal-processing
```

### 2. Create virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Register Jupyter kernel (for experiments)

```bash
python -m ipykernel install --user --name=ecg_env --display-name "Python (ECG Project)"
```

---

## 📂 Data Setup

Due to GitHub file size limits (>100MB), datasets are not included.

### Steps:

1. Download dataset from Kaggle or PhysioNet
2. Create a `data/` folder
3. Add:

   * `mitbih_train.csv`
   * `mitbih_test.csv`

### Quick Demo

Use `test_samples.csv` for instant testing without full dataset.

---

## ▶️ Run the Application

```bash
streamlit run app.py --server.maxUploadSize 500
```

Once launched:

* Upload `test_samples.csv`
* View real-time ECG classification

---

## 🧠 Engineering Highlights

Built with a **production-first mindset**, focusing on:

* Handling large datasets (400MB+)
* Optimizing training time (68 mins ➝ seconds via sampling)
* Building a deployable clinical interface

📌 For detailed challenges and solutions, see `CHALLENGES.md`

---

## 📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

---
