import streamlit as st
import pickle
import pandas as pd
with open('MedInsModel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
st.title('Medical Insurance Cost Prediction')
age = st.number_input('Age', min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', ['female', 'male'])
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=25.0)
children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Smoker', ['no', 'yes'])
region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

sex_encoded = 1 if sex == 'male' else 0
smoker_encoded = 1 if smoker == 'yes' else 0
region_encoded = {'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3}[region]
if st.button('Predict Charges'):
    input_data = {
        'age': age,
        'sex': sex_encoded,
        'bmi': bmi,
        'children': children,
        'smoker': smoker_encoded,
        'region': region_encoded
    }
    print(input_data)
    input_df = pd.DataFrame([input_data])
    predicted_charge = model.predict(input_df)
    st.success(f'Predicted Medical Charges: ${predicted_charge[0]:,.2f}')
