import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("vl_model_useful_features.pkl")
st.write("Using model:", "vl_model_useful_features.pkl")

# Streamlit UI
st.title("Viral Load Prediction App")

user_input = {}
user_input["Age at reporting"] = st.number_input("Enter Age", min_value=0, max_value=120, value=30)
user_input["Sex"] = st.selectbox("Select Sex", ["Male", "Female", "Other"])
regimen_options = ["TDF+3TC+DTG", "AZT+3TC+NVP", "TDF+3TC+EFV", "Other"]
user_input["Current Regimen"] = st.selectbox("Select ART Regimen", regimen_options)
user_input["Last VL Result Clean"] = st.number_input("Enter Last Viral Load Result", min_value=0, value=1000)

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])

# Predict
if st.button("Predict"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Prediction (1 = Suppressed, 0 = Not Suppressed): {prediction[0]}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
