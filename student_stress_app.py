import streamlit as st
import pickle
import numpy as np

# 🎯 Page Configuration
st.set_page_config(page_title="🎓 Student Stress Level Predictor", layout="centered")

# 🧠 Load Model and Scaler
with open("stacking_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# 💡 App Title and Description
st.title("🎯 Student Stress Level Analysis")
st.write("Predict your stress level based on study habits, lifestyle, and academic performance.")

# 🧾 Input Fields
study_hours = st.number_input("📚 Study Hours Per Day", min_value=0.0, max_value=15.0, value=5.0, step=0.5)
extracurricular_hours = st.number_input("🎨 Extracurricular Hours Per Day", min_value=0.0, max_value=10.0, value=1.0, step=0.5)
sleep_hours = st.number_input("😴 Sleep Hours Per Day", min_value=0.0, max_value=12.0, value=7.0, step=0.5)
social_hours = st.number_input("🧑‍🤝‍🧑 Social Hours Per Day", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
physical_activity_hours = st.number_input("💪 Physical Activity Hours Per Day", min_value=0.0, max_value=10.0, value=1.0, step=0.5)
gpa = st.number_input("🎓 GPA", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
academic_performance = st.selectbox("📈 Academic Performance", ["Low", "Medium", "High"])

# 🔢 Encode Academic Performance
performance_encoded = {"Low": 0, "Medium": 1, "High": 2}[academic_performance]

# 🧮 Combine All Inputs
features = np.array([[study_hours, extracurricular_hours, sleep_hours,
                      social_hours, physical_activity_hours, gpa, performance_encoded]])

# ⚙️ Scale Features
features_scaled = scaler.transform(features)

# 🔍 Prediction
if st.button("🔍 Predict Stress Level"):
    prediction = model.predict(features_scaled)[0]

    # Map numeric prediction to labels
    stress_labels = {0: "Low", 1: "Moderate", 2: "High"}
    predicted_label = stress_labels.get(prediction, prediction)

    # 🎉 Display Result
    st.success(f"Your predicted stress level is **{predicted_label}** 🎓")

# ✨ Footer
st.markdown("---")
st.markdown("👨‍💻 *Developed by Yash Dalvi*")
