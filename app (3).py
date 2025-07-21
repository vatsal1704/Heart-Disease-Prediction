 import streamlit as st
import numpy as np
import pickle

# Load your pre-trained model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# UI for user input features
st.title("Heart Disease Prediction")
st.write("Enter patient information below:")

age = st.number_input('Age', min_value=20, max_value=100, value=50)
sex = st.selectbox('Sex', options=['Male', 'Female'])
cp = st.selectbox(
    'Chest Pain Type',
    options=[
        'Typical angina (0)',
        'Atypical angina (1)',
        'Non-anginal pain (2)',
        'Asymptomatic (3)'
    ]
)
trestbps = st.number_input('Resting Blood Pressure (trestbps)', min_value=80, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (chol)', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', options=['No (0)', 'Yes (1)'])
restecg = st.selectbox(
    'Resting ECG Result',
    options=['Normal (0)', 'ST-T wave abnormality (1)', 'Left ventricular hypertrophy (2)']
)
thalach = st.number_input('Max Heart Rate Achieved (thalach)', min_value=60, max_value=210, value=150)
exang = st.selectbox('Exercise Induced Angina (exang)', options=['No (0)', 'Yes (1)'])
oldpeak = st.number_input('ST Depression (oldpeak)', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox(
    'Slope of Peak Exercise ST Segment',
    options=['Upsloping (0)', 'Flat (1)', 'Downsloping (2)']
)
ca = st.selectbox('Number of Major Vessels (ca)', options=[0, 1, 2, 3, 4])
thal = st.selectbox(
    'Thalassemia (thal)',
    options=[
        'Normal (1)', 'Fixed Defect (2)', 'Reversible Defect (3)'
    ]
)

if st.button("Predict"):
    input_features = np.array([[
        age,
        1 if sex == 'Male' else 0,
        int(cp.split('(')[-1][0]),
        trestbps,
        chol,
        int(fbs.split('(')[-1][0]),
        int(restecg.split('(')[-1][0]),
        thalach,
        int(exang.split('(')[-1][0]),
        oldpeak,
        int(slope.split('(')[-1][0]),
        ca,
        int(thal.split('(')[-1][0])
    ]])

    prediction = model.predict(input_features)[0]
    pred_proba = model.predict_proba(input_features)[0][1]

    if prediction == 1:
        st.error(f"Prediction: High risk of Heart Disease (Score: {pred_proba:.2f})")
    else:
        st.success(f"Prediction: Low risk of Heart Disease (Score: {1-pred_proba:.2f})")
