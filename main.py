import streamlit as st
from PIL import Image

import warnings
warnings.filterwarnings('ignore')


import style as style
import home as home
import predictor as predictor
import sobre_bix as sobre
import pbi as pbi


# ----------------------------------SIDEBAR -------------------------------------------------------------
def main():

    style.set_background('images/bg03.jpg')

    st.sidebar.header("Machine Failure predict")
    n_sprites = st.sidebar.radio(
        "Choose an option", options=["Home","Report", "Predictor","About Bix-Tech"], index=0
    )

    #style.spaces_sidebar(15)
    st.sidebar.write('https://www.bixtecnologia.com/')
    image = Image.open('images/logo_sidebar_sem_fundo.png')
    st.sidebar.image(image, use_column_width=True)

    st.image(image, use_column_width=True)  
    
# ------------------------------ CALLING PAGES ----------------------------             

    if n_sprites == "Home":

        home.home()

    if n_sprites == "Report":

        pbi.pbi()

    if n_sprites == "Predictor":

        predictor.predictor()

    if n_sprites == "About Bix-Tech":

        sobre.sobre()        

        
if __name__ == '__main__':
    main()