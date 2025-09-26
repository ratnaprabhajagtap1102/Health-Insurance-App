import streamlit as st
import pickle

st.title('Health Insurance Premium Prediction')

# Age, BMI, Children inputs
age = st.number_input('Age :', min_value=0, max_value=100, step=1, key="age_input")
bmi = st.number_input('BMI :', min_value=0, step=1)
children = st.number_input('Number of Children :', max_value=5, step=1)

# Dropdowns for Gender and Smoker
gender = st.selectbox('Select your gender:', ("Male", "Female"))
smoker = st.selectbox('Do you smoke?', ('No', 'Yes'))

# Load model
model = pickle.load(open('model.pkl','rb'))

# Custom CSS for Predict button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        display: block;
        margin: 20px auto;
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }

    /* Premium output styling */
    .premium-output {
        font-family: 'Verdana', sans-serif;
        font-size: 22px;
        color: #D81B60;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Predict button
if st.button('Predict'):
    gender_val = 0 if gender.upper()=='MALE' else 1
    smoker_val = 0 if smoker.upper()=='NO' else 1
    x_test = [[age, gender_val, bmi, children, smoker_val]]
    yp = round(model.predict(x_test)[0], 2)
    
    # Display output with INR symbol
    st.markdown(f"<div class='premium-output'>Your Premium is: ₹ {yp}</div>", unsafe_allow_html=True)
