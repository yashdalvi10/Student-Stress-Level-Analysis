import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('stacking_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="🎓 Student Stress Level Predictor", layout="centered")

st.title("🎯 Student Stress Level Analysis")
st.write("Predict your stress level based on academic and lifestyle factors.")

# Input fields
sleep_hours = st.number_input("😴 Average Sleep Hours per Day", 0.0, 12.0, 7.0)
study_hours = st.number_input("📚 Average Study Hours per Day", 0.0, 15.0, 5.0)
social_activity = st.number_input("🧑‍🤝‍🧑 Social Activity Hours per Week", 0.0, 30.0, 10.0)
academic_pressure = st.slider("📈 Academic Pressure (1-10)", 1, 10, 5)
attendance = st.slider("🏫 Attendance Percentage", 0, 100, 80)
extracurricular = st.selectbox("🎨 Participates in Extracurricular Activities?", ['Yes', 'No'])

# Encode 'Yes/No'
extracurricular = 1 if extracurricular == 'Yes' else 0

# Combine features
features = np.array([[sleep_hours, study_hours, social_activity, academic_pressure, attendance, extracurricular]])
features_scaled = scaler.transform(features)

# Predict
if st.button("🔍 Predict Stress Level"):
    pred = model.predict(features_scaled)[0]
    st.success(f"Your predicted stress level is **{pred}** 🎓")

st.markdown("---")
st.markdown("👨‍💻 *Developed by Yash Dalvi*")
