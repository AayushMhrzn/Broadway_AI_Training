import streamlit as st
import pandas as pd
import joblib

model = joblib.load("rf_model.joblib")
encoder = joblib.load("rf_encoder.joblib")

st.title("SURVIVOR PREDICTION OF TITANIC")
st.write("Enter passenger details:")

p_class = st.selectbox("Passenger Class:", [1, 2, 3])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age:",step=1)
sibsp = st.number_input("Number of Siblings or Spouses Aboard:",step=1)
parch = st.number_input("Number of Parents or Children Aboard:",step=1)
fare = st.number_input("Fare",value=1.00, step=0.01)

input_df= pd.DataFrame({
    "Pclass":[p_class],
    "Sex":[gender],
    "Age": [age],
    "SibSp":[sibsp],
    "Parch":[parch],
    "Fare":[fare]
})

input_df["Sex"] = encoder.fit_transform(input_df["Sex"])

if st.button("PREDICT:"):
    prediction = model.predict(input_df)[0]
    if prediction ==1:
        st.success("Survived!")
    else:
        st.warning("Didnt Survive!")