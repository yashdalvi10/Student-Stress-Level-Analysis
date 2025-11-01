{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "273833d1-de3d-41e9-991f-2a969a291d55",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load model and scaler\n",
    "model = pickle.load(open('stacking_model.pkl', 'rb'))\n",
    "scaler = pickle.load(open('rf_base_model.pkl', 'rb'))\n",
    "\n",
    "st.set_page_config(page_title=\"🎓 Student Stress Level Predictor\", layout=\"centered\")\n",
    "\n",
    "st.title(\"🎯 Student Stress Level Analysis\")\n",
    "st.write(\"Predict your stress level based on academic and lifestyle factors.\")\n",
    "\n",
    "# Input fields\n",
    "sleep_hours = st.number_input(\"😴 Average Sleep Hours per Day\", 0.0, 12.0, 7.0)\n",
    "study_hours = st.number_input(\"📚 Average Study Hours per Day\", 0.0, 15.0, 5.0)\n",
    "social_activity = st.number_input(\"🧑‍🤝‍🧑 Social Activity Hours per Week\", 0.0, 30.0, 10.0)\n",
    "academic_pressure = st.slider(\"📈 Academic Pressure (1-10)\", 1, 10, 5)\n",
    "attendance = st.slider(\"🏫 Attendance Percentage\", 0, 100, 80)\n",
    "extracurricular = st.selectbox(\"🎨 Participates in Extracurricular Activities?\", ['Yes', 'No'])\n",
    "\n",
    "# Encode 'Yes/No'\n",
    "extracurricular = 1 if extracurricular == 'Yes' else 0\n",
    "\n",
    "# Combine features\n",
    "features = np.array([[sleep_hours, study_hours, social_activity, academic_pressure, attendance, extracurricular]])\n",
    "features_scaled = scaler.transform(features)\n",
    "\n",
    "# Predict\n",
    "if st.button(\"🔍 Predict Stress Level\"):\n",
    "    pred = model.predict(features_scaled)[0]\n",
    "    st.success(f\"Your predicted stress level is **{pred}** 🎓\")\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"👨‍💻 *Developed by Yash Dalvi*\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
