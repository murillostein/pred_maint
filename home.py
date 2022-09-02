import streamlit as st
from PIL import Image

def home():
    st.title('')               
    st.title('Machine Failure Predictor')
    st.subheader('Predict if a machine will fail based on its operations conditions and analyse the data!')
    image = Image.open('images/home.png')
    st.image(image, use_column_width=True)

    st.subheader('What is this app?')
    st.write('This app is a digital solution to manage industrial operations. It utilizes Industry 4.0 principles and improve the effiency of resources allocation.')
    st.write('It contains a report with data about the current state of machines at an industrial plant. With it, it is possible to keep track about the machines demand.')
    

    st.subheader('Try by yourself, it is free!')
    st.write('At the Predict page, you can input your data and visualize the predicted state of the machine!')

        