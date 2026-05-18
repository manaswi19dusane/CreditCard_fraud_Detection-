import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load(r"C:\Users\Manswi R. dusane\Documents\fraud_detection_model.pkl")

st.set_page_config(page_title="Fraud Detection System", layout="wide")

st.title("💳 Credit Card Fraud Detection")
st.markdown("### Detect fraudulent transactions using a Machine Learning model")

# Sidebar navigation
mode = st.sidebar.radio("Choose Mode", ["Single Transaction", "Batch Prediction (CSV Upload)"])

# --- Single Transaction Mode ---
if mode == "Single Transaction":
    st.subheader("🔹 Enter Transaction Details")

    time = st.number_input("Transaction Time", value=0.0)
    amount = st.number_input("Transaction Amount", value=0.0)

    # Fill V1–V28 with zeros (dummy)
    features = [0.0] * 28
    input_data = [time, amount] + features

    if st.button("Predict Transaction"):
        final_features = np.array(input_data).reshape(1, -1)
        prediction = model.predict(final_features)[0]
        probability = model.predict_proba(final_features)[0][1]

        if prediction == 1:
            st.error(f"🚨 Fraud Detected! (Probability: {probability:.2f})")
        else:
            st.success(f"✅ Legitimate Transaction (Probability of Fraud: {probability:.2f})")

# --- Batch Prediction Mode ---
else:
    st.subheader("🔹 Upload CSV File of Transactions")
    uploaded_file = st.file_uploader("Upload your transaction CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("📊 Uploaded Data Preview", df.head())

        if st.button("Run Fraud Detection"):
            # Run predictions
            predictions = model.predict(df)
            probabilities = model.predict_proba(df)[:, 1]

            df["Fraud_Prediction"] = predictions
            df["Fraud_Probability"] = probabilities

            st.write("✅ Prediction Results", df.head(20))

            # Fraud distribution chart
            fraud_count = df["Fraud_Prediction"].value_counts()
            fig, ax = plt.subplots()
            fraud_count.plot(kind="pie", autopct="%1.1f%%", labels=["Legit", "Fraud"], ax=ax)
            ax.set_ylabel("")
            ax.set_title("Fraud vs Legit Distribution")
            st.pyplot(fig)

            # Download results
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Predictions as CSV",
                data=csv,
                file_name="fraud_detection_results.csv",
                mime="text/csv",
            )
