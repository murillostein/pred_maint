import streamlit as st
from PIL import Image

def sobre():
    st.title('')  

    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.title("About us")
    with col3:
        st.write("")             

    image = Image.open('images/sobre_nos.png')
    st.image(image, use_column_width=True)
    st.write('We are a data business intelligence and data science consultancy focused on business and achieving results. We use the main tools and technologies of the market in the development of projects that help our clients extract the maximum value from their data and transform themselves digitally. Thus, we believe that the management of processes and people is optimized, which facilitates and improves everyone’s life.')
    st.write('BIX Tecnologia was founded in Florianópolis in 2014 by engineer Felipe Santos Eberhardt, who realized the market’s need to start using data to create more efficient strategies and assertive decision making. Without investors or accelerators, he started to win customers, increase the team and develop several business intelligence projects.')
    st.write('Since then, BIX Tecnologia’s growth has been solid, thanks to a team with an analytical profile and training in the main technology areas, winning customers all over Brazil, developing projects in the most diverse sectors of organizations and with a complete and vast portfolio that encompasses the various verticals of the economy.')

    st.header('')
    st.subheader('Contact us')
    image = Image.open('images/contato.png')
    st.image(image, use_column_width=True)


    
    st.write('Phone: +55 (47) 99981 0094 / +1 954 607 7944')
    st.write('Email : contato@bixtecnologia.com.br')