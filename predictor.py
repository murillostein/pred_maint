import streamlit as st
import pandas as pd
import pickle

def predictor():
    # --------MAIN------

    st.title("Predict machine state")

    st.write("Predictive Maintenance is the most efficient approach to managing and allocating resources to industrial operations.")
    st.write("This app helps your industry to utilize this approach and monitor more precisely the actual machine state.")



    # -------USER INPUTS----------
    st.title("Define machine current status.")
    st.markdown("")
    col1, col2 = st.columns(2)
    with col1:
        In1 =  st.selectbox('Type',['High', 'Medium', 'Low'])
        In2 =  st.number_input("Air Temperature [ºC]", min_value=290 , max_value=350,step=2)
        In3 =  st.number_input("Process Temperature [ºC]", min_value=290, max_value=350,step=2)
        

    with col2:
        In4 =  st.number_input("Rotational Speed [rpm]", min_value=800,max_value=2500,step=50)
        In5 =  st.number_input("Torque [Nm]", min_value=8,max_value=120,step=5)
        In6 =  st.number_input("Tool Wear [min]", min_value=0, max_value=300, step=5)


    st.markdown("")
    
    param = [[In1,In2,In3,In4,In5,In6,0,0,0]]

    df = pd.DataFrame(param,columns=['Type','Air Temperature [K]', 'Process Temperature [K]','Rotational speed [rpm]', 'Torque [Nm]', 'Tool Wear [min]','High', 'Low','Medium'])

    # Data preprocessing 
    df[In1] = 1
    df.drop("Type",axis=1, inplace=True)
    df['var_temperature'] = df['Process Temperature [K]'] - df['Air Temperature [K]']


    # make the prediction
    btn_predict = st.button("Predict")

    if btn_predict:

        filename = 'model/finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        st.header("Result")

        results = loaded_model.predict(df)

        st.write('The  state of the machine is: ' , results.item())