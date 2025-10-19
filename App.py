import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load the trained model
# -----------------------------
model_path = 'medical.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.title("Medical Cost Prediction App")

# -----------------------------
# Create two columns
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# User Inputs
# -----------------------------
with col1:
    age = st.number_input('Age', min_value=0, max_value=120)
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0)
    children = st.number_input('Number of Children', min_value=0, max_value=10)

with col2:
    sex = st.selectbox('Sex', ['male', 'female'])
    smoker = st.selectbox('Smoker', ['yes', 'no'])
    region = st.selectbox('Region', ['northeast','northwest','southeast','southwest'])

# -----------------------------
# Encode categorical variables (Label Encoding)
# -----------------------------
sex_encoded = 1 if sex == 'male' else 0
smoker_encoded = 1 if smoker == 'yes' else 0

region_mapping = {'northeast':0, 'northwest':1, 'southeast':2, 'southwest':3}
region_encoded = region_mapping[region]

# -----------------------------
# Predict
# -----------------------------
if st.button('Predict'):
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    prediction = model.predict(input_data)
    st.success(f'Estimated Medical Cost: ${prediction[0]:.2f}')
