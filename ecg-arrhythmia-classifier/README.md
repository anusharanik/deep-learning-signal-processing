ECG Arrhythmia Classifier

A production-ready deep learning pipeline designed to classify ECG heartbeats into five clinical categories. This project bridges the gap between advanced signal processing and clinical reporting, providing a functional dashboard for medical professionals.
🚀 Key Features
1D-CNN Architecture: Optimized for spatial morphology detection in cardiac signals.
Real-time Visualization: Interactive ECG waveform rendering using Streamlit.
Batch Processing: High-speed classification of thousands of heartbeats in seconds.
Clinical Reporting: Automated PDF generation with diagnostic summaries and confidence levels.
Data Balancing: Integrated SMOTE to ensure high sensitivity for rare arrhythmias.
📁 Project Structure
ecg-arrhythmia-classifier
.
├── data/                  # Local folder for large datasets (Download required)
│   ├── mitbih_train.csv
│   └── mitbih_test.csv
├── sample-outputs/        # Screenshots demonstrating app functionality
│   ├── single_analysis_1.png
│   ├── single_analysis_2.png
│   ├── batch_processing_1.png
│   └── batch_processing_2.png
├── app.py                 # Streamlit dashboard & clinical interface
├── experiments.ipynb      # Training, SMOTE balancing, and 1D-CNN logic
├── ecg_lstm_model.keras   # Saved 1D-CNN model weights
├── scaler.pickle          # Saved StandardScaler for signal normalization
├── requirements.txt       # Project dependencies (Python 3.13 compatible)
├── README.md              # Main project documentation
├── CHALLENGES.md          # Technical engineering retrospective
├── test_samples.csv       # Small demo file (Included for instant testing)
└── sample_test.csv        # Secondary demo file (Included)


📊 Dataset: MIT-BIH Arrhythmia
The model uses the MIT-BIH Arrhythmia Database, a gold-standard collection of ambulatory ECG recordings.
Class Distribution (Original)
Label	Category	Count
0	Normal (N)	72,471
1	Supraventricular (S)	2,223
2	Ventricular (V)	5,788
3	Fusion (F)	641
4	Unclassifiable (Q)	6,431
Note: SMOTE was applied to the training set to resolve this heavy class imbalance and ensure high sensitivity for rare arrhythmias.
🛠️ Installation & Setup
1. Clone the Repository
bash
git clone https://github.com
cd ecg-classifier


2. Setup Virtual Environment
bash
#Create and activate environment
python -m venv venv
.\venv\Scripts\activate

#Install project dependencies
pip install -r requirements.txt

# REGISTER THE KERNEL FOR JUPYTER (Crucial for experiments.ipynb)
python -m ipykernel install --user --name=ecg_env --display-name "Python (ECG Project)"

3. Local Data Setup
Due to GitHub file size limits (>100MB), the full CSV files are not included.
Download data from Kaggle or PhysioNet.
Create a data/ folder and place mitbih_train.csv and mitbih_test.csv inside it.
Demo Mode: Use the included test_samples.csv to test the app immediately without the full dataset.

4. Run the Application

Note: When opening experiments.ipynb, ensure you select the "Python (ECG Project)" kernel to use the correct dependencies.

bash
streamlit run app.py --server.maxUploadSize 500

5. Instant Demo: Once the app opens in your browser, upload the test_samples.csv file from the root folder to see the 1D-CNN in action immediately.

🧠 Engineering Retrospective
This project was built with a "Production-First" mindset. Significant effort was placed on resolving real-world deployment issues, such as handling 400MB+ datasets and optimizing training from 68-minute epochs down to seconds via stratified sampling.

For full details on these technical solutions, see the CHALLENGES.md file.





