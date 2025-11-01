🧠 Student Stress Level Analysis using Machine Learning
  🎓 A Machine Learning approach to understand and predict student stress levels based on lifestyle, academic, and personal factors.

🌟 Project Overview
Student mental health is one of the most pressing issues today.
This project aims to analyze various factors — like sleep, study hours, academic pressure, and social support — to predict stress levels (Low, Moderate, High) using Supervised Machine Learning.

🎯 Key Objectives
Identify patterns and correlations between lifestyle and stress
Build models that predict student stress levels
Evaluate multiple ML algorithms for best performance
Derive actionable insights for stress management


📊 Dataset Information
| Feature Type       | Description                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| 🎯 **Target**      | Stress_Level → {Low, Moderate, High}                                                 |
| 📁 **Features**    | Sleep Hours, Study Hours, Academic Pressure, Physical Activity, Social Support, etc. |
| 🔢 **Records**     | ~2000+ (varies)                                                                      |
| 🧩 **File Format** | CSV                                                                                  |


🧹 Data Preprocessing Steps
Removed duplicates & handled missing values
Dropped irrelevant columns (Student_ID)
Label encoded Stress_Level (Low→0, Moderate→1, High→2)
Used RobustScaler to minimize the effect of outliers
Performed train-test split (80–20 ratio)


📈 Exploratory Data Analysis (EDA)
✨ Visualized relationships using:
Histograms & KDE plots (Feature Distribution)
Boxplots (Outlier Detection)
Correlation Heatmap
Pairplots (Multivariate Trends)

🔍 Insights Example:
High academic pressure → higher stress
More sleep hours → lower stress
Physical activity reduces stress probability


🤖 Machine Learning Models Used
| Model               | Type          | Accuracy                | Remark                                |
| ------------------- | ------------- | ----------------------- | ------------------------------------- |
| Logistic Regression | Linear Model  | ⭐ Good baseline        | Fast and interpretable                |
| Decision Tree       | Non-linear    | 🌿 Decent accuracy      | Handles non-linearity well            |
| Random Forest       | Ensemble      | 🏆 **Best Performance** | Balanced & robust                     |
| Stacking Classifier | Meta Ensemble | 💡 Excellent            | Combines strengths of multiple models |


🧮 Evaluation Metrics:
Accuracy | Precision | Recall | F1-Score | Confusion Matrix | ROC-AUC


🏆 Results Summary
Random Forest & Stacking Classifier achieved the best overall accuracy
Balanced recall across all stress levels
Clear interpretability of key stress-driving features

📊 Example Result Visualization:
Model Accuracy:
- Logistic Regression → 82%
- Decision Tree → 85%
- Random Forest → 92%
- Stacking Classifier → 95%


💻 Tech Stack
| Category               | Tools & Libraries                                |
| ---------------------- | ------------------------------------------------ |
| 🐍 Language            | Python                                           |
| 📚 Libraries           | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn |
| 🧰 Environment         | Jupyter Notebook                                 |
| 🚀 Optional Deployment | Streamlit / Flask                                |


🚀 How to Run
# Clone the repo
git clone https://github.com/yashdalvi10/Student-Stress-Level-Analysis.git

# Navigate to folder
cd Student-Stress-Level-Analysis

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Student_stress_Level_Analysis.ipynb


🔮 Future Enhancements
✨ Deploy the model on Streamlit for real-time predictions
📈 Add SHAP / LIME for model interpretability
📊 Build a dashboard for visual analytics
💬 Collect real-world student data through surveys


👨‍💻 Author
Yash R. Dalvi || ydalvi565@gmail.com
📧 Data Science & Machine Learning Enthusiast
💼 Passionate about solving real-world problems using data


🔥 “Predicting stress today to prevent burnout tomorrow.”
