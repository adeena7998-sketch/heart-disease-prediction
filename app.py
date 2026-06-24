import streamlit as st
import pickle
import numpy as np

# Load model
with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient information below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)

trestbps = st.number_input("Resting Blood Pressure")

chol = st.number_input("Cholesterol")

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])

restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2)

thalach = st.number_input("Maximum Heart Rate")

exang = st.selectbox("Exercise Induced Angina", [0, 1])

oldpeak = st.number_input("Oldpeak", format="%.2f")

slope = st.number_input("Slope (0-2)", min_value=0, max_value=2)

ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4)

thal = st.number_input("Thal (0-3)", min_value=0, max_value=3)

# Prediction button
if st.button("Predict"):

    features = np.array([[age, sex, cp, trestbps, chol,
                          fbs, restecg, thalach,
                          exang, oldpeak, slope,
                          ca, thal]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")
