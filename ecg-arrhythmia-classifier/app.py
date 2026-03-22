import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import io
from fpdf import FPDF
from tensorflow.keras.models import load_model

st.set_page_config(page_title="ECG Classifier Pro", layout="wide")

# Load Model and Scaler
@st.cache_resource
def load_assets():
    model = load_model('ecg_lstm_model.keras')
    with open('scaler.pickle', 'rb') as handle:
        scaler = pickle.load(handle)
    return model, scaler

try:
    model, scaler = load_assets()
except Exception as e:
    st.error(f"🚨 Model or Scaler not found! Error: {e}")
    st.stop()

CLASSES = {0: 'Normal (N)', 1: 'Supraventricular (S)', 2: 'Ventricular (V)', 3: 'Fusion (F)', 4: 'Unclassifiable (Q)'}

st.title("🫀 ECG Arrhythmia Classifier (1D-CNN)")

uploaded_file = st.file_uploader("Upload MIT-BIH CSV", type="csv")

if uploaded_file:
    # Create Tabs for Single vs Batch
    tab1, tab2 = st.tabs(["🔍 Single Analysis", "📊 Batch Processing"])

    with tab1:
        # Reset file pointer to the beginning
        uploaded_file.seek(0)
        
        # Load only enough for the selector
        data = pd.read_csv(uploaded_file, header=None, nrows=22000) 
        row_idx = st.number_input("Select Row Index", min_value=0, max_value=len(data)-1, value=0)
        
        # ... [Your existing Single Analysis code here] ...
        signal = data.iloc[row_idx, :187].values
        st.subheader(f"ECG Signal Visualization (Row {row_idx})")
        st.line_chart(signal)
        
        if st.button("Predict Single"):
            scaled = scaler.transform(signal.reshape(1, -1)).reshape(1, 187, 1)
            pred_probs = model.predict(scaled, verbose=0).flatten() # Flatten to 1D
            predicted_class = np.argmax(pred_probs)
            
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"### Diagnosis: **{CLASSES[predicted_class]}**")
                prob_df = pd.DataFrame({'Category': list(CLASSES.values()), 'Confidence': [f"{p*100:.2f}%" for p in pred_probs]})
                st.table(prob_df)
            with col2:
                st.bar_chart(pd.DataFrame({'Prob': pred_probs}, index=list(CLASSES.values())))

    with tab2:
        st.subheader("Batch Summary Report")
        num_rows = st.slider("How many rows to scan?", 100, 10000, 1000)
        
        if st.button(f"Run Batch Analysis on {num_rows} Rows"):
            # IMPORTANT: Reset file pointer again before batch read
            uploaded_file.seek(0)
            
            with st.spinner("Processing heartbeats..."):
                # Load the requested chunk
                batch_data = pd.read_csv(uploaded_file, header=None, nrows=num_rows)
                signals = batch_data.iloc[:, :187].values
                
                # Scale and Predict
                scaled_batch = scaler.transform(signals).reshape(len(signals), 187, 1)
                batch_preds = model.predict(scaled_batch, verbose=0)
                results = np.argmax(batch_preds, axis=1)
                
                # Count and Map Labels
                counts = pd.Series(results).map(CLASSES).value_counts()
                
                # Display Results
                c1, c2 = st.columns(2)
                with c1:
                    st.write("#### Arrhythmia Counts")
                    st.dataframe(counts)
                with c2:
                    st.write("#### Distribution %")
                    st.bar_chart(counts)
                
                st.success(f"Analyzed {num_rows} heartbeats successfully!")




        st.info("💡 Note: This model was trained on a 5% subset of the MIT-BIH dataset for experimental purposes.")
