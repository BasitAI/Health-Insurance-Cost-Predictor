import streamlit as st
from prediction_helper import predict

# Set the page configuration
st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide", page_icon="💡")

# Page title and description
st.title("🌟 Health Insurance Cost Predictor")
st.markdown(
    """
    Welcome to the Health Insurance Cost Predictor!  
    Enter the required details below, and click on **Predict** to get your insurance cost estimate.  
    _Designed with ❤️ by Basit Shabir._
    """
)

# Input fields
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', 'Other'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Define the layout
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("🧑 Age", min_value=18, max_value=100, step=1)
    gender = st.selectbox("🚻 Gender", categorical_options["Gender"])
    marital_status = st.selectbox("💍 Marital Status", categorical_options["Marital Status"])

with col2:
    number_of_dependants = st.number_input("👨‍👩‍👧‍👦 Number of Dependants", min_value=0, max_value=20, step=1)
    bmi_category = st.selectbox("⚖️ BMI Category", categorical_options["BMI Category"])
    smoking_status = st.selectbox("🚬 Smoking Status", categorical_options["Smoking Status"])

with col3:
    income_lakhs = st.number_input("💵 Income (in Lakhs)", min_value=0, max_value=200, step=1)
    genetical_risk = st.number_input("🧬 Genetical Risk (0-5)", min_value=0, max_value=5, step=1)
    region = st.selectbox("📍 Region", categorical_options["Region"])

# More inputs
insurance_plan = st.selectbox("💼 Insurance Plan", categorical_options["Insurance Plan"])
employment_status = st.selectbox("👔 Employment Status", categorical_options["Employment Status"])
medical_history = st.selectbox("🩺 Medical History", categorical_options["Medical History"])

# Create a dictionary for input values
input_dict = {
    "Age": age,
    "Number of Dependants": number_of_dependants,
    "Income in Lakhs": income_lakhs,
    "Genetical Risk": genetical_risk,
    "Insurance Plan": insurance_plan,
    "Employment Status": employment_status,
    "Gender": gender,
    "Marital Status": marital_status,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Region": region,
    "Medical History": medical_history
}

# Prediction button
st.markdown("---")
if st.button("💡 Predict"):
    try:
        prediction = predict(input_dict)
        st.success(f"🎉 Predicted Health Insurance Cost: **{prediction}**")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
