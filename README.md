# ❤️ Heart Disease Prediction App

## 🔍 Project Overview

The **Heart Disease Prediction App** is an interactive web tool built using **Streamlit** that leverages machine learning to predict the likelihood of a person having heart disease based on clinical input parameters. This tool is designed to assist healthcare professionals and individuals in making preliminary assessments based on common risk factors.

### 🎯 Purpose

Heart disease remains one of the leading causes of death globally. Early detection is crucial in reducing associated risks. This project aims to provide a simple yet effective way to:

- Analyze patient data inputs.
- Predict the risk of heart disease using a trained machine learning model.
- Offer a user-friendly interface for real-time predictions.

### 🧠 Methodology

- **Dataset Used:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Model:** Logistic Regression (with preprocessing using `StandardScaler`)
- **Framework:** Python, Scikit-learn, Streamlit
- **Deployment:** Streamlit Cloud

### 🛠️ Features

- Interactive sliders and dropdowns for inputting patient data.
- Real-time predictions of heart disease risk.
- User-friendly UI built with Streamlit.
- Portable and open-source – easily extendable or deployable.

---

## 🚀 Live Demo

👉 **[Click here to try the app!]https://heart-disease-predictionnn.streamlit.app/**

> No installation required – access directly from your browser!


## 📝 How to Use

1. Enter patient details like age, cholesterol levels, blood pressure, etc.
2. Click the **Predict** button.
3. The app will display whether the person is at risk of heart disease or not.

---

## 📦 Installation (For Local Use)

```bash
# Clone the repository
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
