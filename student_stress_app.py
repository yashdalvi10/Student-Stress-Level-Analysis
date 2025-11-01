{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "273833d1-de3d-41e9-991f-2a969a291d55",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-01 23:25:21.769 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:21.771 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.498 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-11-01 23:25:22.500 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.500 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.501 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.501 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.502 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.505 Session state does not function when running a script without `streamlit run`\n",
      "2025-11-01 23:25:22.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.506 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.508 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.508 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.510 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.511 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.512 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.513 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.515 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.516 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.516 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.516 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.518 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.522 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.524 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.524 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-01 23:25:22.526 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'RandomForestClassifier' object has no attribute 'transform'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 27\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[38;5;66;03m# Combine features\u001b[39;00m\n\u001b[0;32m     26\u001b[0m features \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([[sleep_hours, study_hours, social_activity, academic_pressure, attendance, extracurricular]])\n\u001b[1;32m---> 27\u001b[0m features_scaled \u001b[38;5;241m=\u001b[39m \u001b[43mscaler\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtransform\u001b[49m(features)\n\u001b[0;32m     29\u001b[0m \u001b[38;5;66;03m# Predict\u001b[39;00m\n\u001b[0;32m     30\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m st\u001b[38;5;241m.\u001b[39mbutton(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m🔍 Predict Stress Level\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'RandomForestClassifier' object has no attribute 'transform'"
     ]
    }
   ],
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f905480a-d537-4cc4-ab73-17b6d1a3b852",
   "metadata": {},
   "outputs": [],
   "source": []
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
