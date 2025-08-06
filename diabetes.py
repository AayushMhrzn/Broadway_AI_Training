import streamlit as st
import pandas as pd
import joblib
import numpy as np

our_model = joblib.load("logistic_regression_model.joblib")
scaler = joblib.load("scaler.joblib")

st.title("Diabetes Prediction App")
st.write("Please enter the following patient information:")

#inputs haru
Age = st.number_input("Age", min_value=0, max_value=120, value=30)
Pregnancy = st.number_input("Pregnancy (number of times)", min_value=0, max_value=20, value=1)
BMI = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=60.0, value=22.0, step=0.1)
Glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0, value=100.0, step=0.1)
BloodPressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0, step=0.1)
HbA1c = st.number_input("HbA1c (%)", min_value=0.0, max_value=15.0, value=5.5, step=0.1)
LDL = st.number_input("LDL (mg/dL)", min_value=0.0, max_value=300.0, value=100.0, step=0.1)
HDL = st.number_input("HDL (mg/dL)", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
Triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=0.0, max_value=500.0, value=150.0, step=0.1)
WaistCircumference = st.number_input("Waist Circumference (cm)", min_value=0.0, max_value=200.0, value=80.0, step=0.1)
HipCircumference = st.number_input("Hip Circumference (cm)", min_value=0.0, max_value=200.0, value=90.0, step=0.1)

#calculate WHR
WHR = round(WaistCircumference / HipCircumference, 2) if HipCircumference != 0 else 0.0
#st.write(f"Waist-to-Hip Ratio (WHR): **{WHR}**")

features = np.array([[Age, Pregnancy, BMI, Glucose, BloodPressure, HbA1c, LDL, HDL,
                      Triglycerides, WaistCircumference, HipCircumference, WHR]])

scaled = scaler.transform(features)

if st.button("PREDICT"):
    pred = our_model.predict(scaled)[0]
    st.subheader("Prediction Result:")
    if pred == 1:
        st.warning("You have Diabetes.")
    else:
        st.success("You do not have Diabetes.")
