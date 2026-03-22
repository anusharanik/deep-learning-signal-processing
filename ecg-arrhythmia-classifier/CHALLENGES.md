Technical Challenges & Engineering Solutions
Project: ECG Arrhythmia Classifier (1D-CNN / LSTM)
Developer: Anusha Rani Katta

This document serves as a technical retrospective on the engineering hurdles encountered while building a production-ready ECG diagnostic tool and the strategies used to overcome them.
1. The "Big Data" Bottleneck (Training Optimization)
The Problem: Initial training on the full MIT-BIH dataset (over 100,000 records) was computationally unsustainable on a local machine. The first epoch exceeded 68 minutes of execution time without completing, preventing iterative testing and hyperparameter tuning.
The Solution: Implemented a 5% Stratified Data Slice. By selecting a representative subset of the data, I reduced training time from hours to seconds while maintaining the relative proportions of each arrhythmia class.
The Result: This "Lean AI" approach allowed for rapid prototyping between LSTM and 1D-CNN architectures. Despite the reduced data volume, the model achieved 99.87% confidence on Fusion (F) beats, proving that architectural quality can often outweigh raw data volume in the prototyping phase.

2. Architectural Evolution: LSTM to 1D-CNN
The Problem: While LSTMs are effective for sequences, they were computationally heavy for high-frequency ECG data, leading to slower inference in the live Streamlit app.
The Solution: Transitioned the core engine to a 1D-Convolutional Neural Network (1D-CNN).
The Result: 1D-CNNs are superior at "scanning" the spatial morphology (shape) of a heartbeat—such as QRS width and P-wave presence. This shift resulted in near-instant classification and more stable detection of "wide" arrhythmias like Ventricular (V) beats.

3. Big Data Memory Management (400MB+ CSVs)
The Problem: The mitbih_train.csv file (400MB+) exceeded Streamlit’s default 200MB upload limit. Even when allowed, loading the full file into RAM caused the application to freeze.
The Solution:
Server Flags: Launched the app with --server.maxUploadSize 500.
Optimized I/O: Modified the data pipeline to use pd.read_csv(nrows=1000).
The Result: The app handles massive clinical datasets instantly by loading a manageable "preview" for analysis rather than the entire database.

4. File Stream "Exhaustion" in Multi-Tab UI
The Problem: The app crashed when switching between "Single Analysis" and "Batch Processing" tabs. This occurred because the Python file pointer remained at the end of the file after the first read.
The Solution: Implemented low-level buffer management using uploaded_file.seek(0).
The Result: This "rewinds" the data stream, allowing the user to perform multiple independent analyses on the same file without a session crash.

5. Windows-Specific Hardware Detection Bug
The Problem: The SMOTE library (used to balance the dataset) failed with a ValueError: found 0 physical cores < 1 due to a hardware detection bug in the loky library on Windows.
The Solution: Manually bypassed the core-count check by setting the environment variable os.environ['LOKY_MAX_CPU_COUNT'] = '4'.
The Result: Successfully balanced the minority classes (Fusion and Supraventricular), ensuring the model didn't just "default" to predicting Normal beats.

6. Bridging the Gap to Clinical Reporting
The Problem: AI predictions in a terminal are not useful for medical technicians.
The Solution: Built a dynamic PDF Export Engine using fpdf2 and io.BytesIO. I resolved a byte-encoding AttributeError by properly wrapping the PDF output into a bytes() object for browser-side downloading.
The Result: Technicians can now generate a professional, timestamped diagnostic report including the waveform and confidence scores in one click.


Industry Impact & Clinical Utility:
The engineering solutions developed in this project directly address the primary hurdles of Digital Health Deployment:
Scalability: Solving the 400MB memory bottleneck proves the capability to handle high-resolution, long-term ambulatory monitoring data.
Clinician-Centric Design: Moving from terminal-based predictions to a dynamic PDF Reporting engine demonstrates a commitment to the "end-user"—ensuring AI insights are documented, shareable, and clinically actionable.
Pragmatic Development: Pivoting to a Stratified 5% Data Slice shows a resource-aware approach to AI, achieving high-confidence results (99% for Fusion beats) while significantly reducing computational overhead and iteration time.