import streamlit as st
from PIL import Image

def home():
    st.title('')               
    st.title('Machine Failure Predictor')
    st.subheader('Predict if a machine will fail based on its operations conditions!')
    image = Image.open('images/home.png')
    st.image(image, use_column_width=True)

    st.subheader('What is this app?')
    st.write('This app is a digital solution for managing industrial operations. It helps industry management by presenting a report about key business indicators and a tool for monitoring machine conditions.')
    st.write('By utilizing it, you allocate your resources in a more assertive and efficient way.')
    

    st.subheader('Try by yourself, it is free!')
    st.write('At the Predict page, you can input your data and visualize the predicted state of the machine!')

        