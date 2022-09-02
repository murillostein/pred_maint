import streamlit as st
from PIL import Image

def pbi():
    st.title("Power BI report")
    st.subheader("Keep track of you industry operations in real time!")
    
    st.components.v1.iframe('https://app.powerbi.com/view?r=eyJrIjoiNjExMjI3OWMtNGVjNC00Zjg1LTk5OGEtMzhjODI2NWRlOWY4IiwidCI6IjgzZmI1ZTc2LWRiMWItNGM0YS1iZDIwLTA5Nzg0ZDRkYzEyOCJ9', height=400)