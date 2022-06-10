# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 01:36:55 2022

@author: Dilsh Sula
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


loaded_model = pickle.load(open('card.sav', 'rb'))


def cardio_dtct(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Coronary Heart Disease'
    else:
      return 'The Person has a Coronary Heart Disease'
      

def main():
    
    st.header('MedXpert©️')
    
    st.subheader('Cardiovascular Disease Predictor')
    
    with st.sidebar:
        
        selected = option_menu('Group Members',
                              
                              ['Dilshan   - 2019521460115',
                               'Chamara - 2019521460117',
                               'Haritha   - 2019521460116'],
                              icons=['person-circle','person-circle','person-circle'],default_index=-1)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sbp = st.text_input('Systolic Blood Pressure Value')
        
    with col2:
        tobacco = st.text_input('Cumulative Tobacco Quantity (Kg)')
        
    with col3:
        ldl = st.text_input('Low Density Lipoprotein Cholesterol')
        
    with col1:
        adiposity = st.text_input('Adiposity Value')
        
    with col2:
        famhist = st.text_input('Family History of Heart Disease','Present = 1  |  Absent = 0')
        
    with col3:
        typea = st.text_input('Type-A Behavior')
        
    with col1:
        obesity = st.text_input('Obesity Value')
        
    with col2:
        alcohol = st.text_input('Current Alcohol Consumption Value')
        
    with col3:
        age = st.text_input('Age at Onset')
    
    
    dtct = ''
    
    
    if st.button('Predict Cardiovascular Disease'):
        dtct = cardio_dtct([sbp,tobacco,ldl,adiposity,famhist,typea,obesity,alcohol,age])
        
    st.success(dtct)
    
   
if __name__ == '__main__':
    main()