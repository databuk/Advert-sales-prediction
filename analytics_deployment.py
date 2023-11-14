import streamlit as st
import pandas as pd
import numpy as np
import joblib

pipeline = joblib.load('advert_pipeline.joblib')

def take_user_input():
    st.title('Advert Sales Analytics Prediction App')
    st.write('Enter data')
    tv =st.number_input('TV ($1000)', 0, 1000, 10)
    radio = st.number_input('Radio ($1000)', 0, 1000, 25)
    newspaper = st.number_input('Newspaper ($1000)', 0, 1000, 30)
    user_input = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    return user_input
    
input_data = take_user_input()

if st.button('Predict'):
    prediction = pipeline.predict(input_data)
    st.success(f'The total sales generated from advert is ${np.round(prediction[0], 2)}million.')
    