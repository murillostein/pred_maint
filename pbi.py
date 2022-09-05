import streamlit as st
from PIL import Image

def pbi():
    st.set_page_config(  # Alternate names: setup_page, page, layout
        layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title=None,  # String or None. Strings get appended with "• Streamlit". 
        page_icon=None,  # String, anything supported by st.image, or None.
    )


    st.title("Power BI report")
    st.subheader("Keep track of you industry operations in real time!")
    
    st.components.v1.iframe('https://app.powerbi.com/view?r=eyJrIjoiNjExMjI3OWMtNGVjNC00Zjg1LTk5OGEtMzhjODI2NWRlOWY4IiwidCI6IjgzZmI1ZTc2LWRiMWItNGM0YS1iZDIwLTA5Nzg0ZDRkYzEyOCJ9', height=400)
