import streamlit as st
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import joblib
import pickle
oe=OrdinalEncoder()
st.title("Industrial Copper Modelling")


st.markdown(
    """<div style="text-align: right; margin-right: 50px;">
        <h3 style="color: #1E90FF;">- Created by Gokulraj Pandiyarajan</h3>
    </div>""",
    unsafe_allow_html=True
)
st.write()

st.markdown(
    """
    <style>
    .stButton {
        color: green; /* Set the text color */
        padding: 10px 20px; /* Adjust padding to increase button size */
        font-size: 18px; /* Set the font size */    
        border-radius: 10px; /* Add rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """<div style="background-color: #f0f0f0; padding: 10px; border-radius: 10px;">
        <p style="font-size: 20px;">An industrial copper modeling problem typically involves the development of mathematical, 
        statistical, or machine learning models to predict or optimize various aspects related to the production, utilization, 
        or market behavior of copper in an industrial context.</p>
    </div>""",
    unsafe_allow_html=True
)
st.markdown(
    """<div style="text-align: center;">
        <h3 style="color: #1A03FE;"> Choose The Task</h3>
    </div>""",
    unsafe_allow_html=True
)

selected_option = st.selectbox("", 
                               ("Choose The Option","Regression", "Classification"))
if selected_option=='Regression':
    quantity_tons = st.text_input("Enter Quantity tons")
    #quantity_tons=st.number_input('Quantity Tons', min_value=-2000, max_value=1000000000, value=0, step=1)
    status= st.selectbox("Choose the Status",("","Draft","Lost","Not lost for AM","Offerable","Offered","Revised","To be approved","Won","Wonderful"))
    item_type=st.selectbox("Choose the Item type",("","IPL","Others","PL","S","SLAWR","W","WI"))
    application=st.number_input("Appication",min_value=2,max_value=99, value=2, step=1)
    thickness=st.text_input("Enter Thickness")
    #thickness=st.number_input("Thickness",min_value=0,max_value=2500, value=0, step=1)
    width=st.number_input("Width",min_value=1,max_value=2990, value=1, step=1)
    country=st.number_input("Country",min_value=25,max_value= 113, value=25, step=1)
    customer= st.number_input("Customer",min_value=12458,max_value= 30408185, value=12458, step=1)
    product_ref=st.number_input("Product Ref",min_value=611728,max_value= 1722207579, value=611728, step=1)    
    predict=st.button("Predict")
    if predict:
        quantity_tons=float(quantity_tons)
        thickness=float(thickness)
        if quantity_tons >=-2000 and quantity_tons <=1000000000:
            pass
        else:
            st.error("Quantity Tons Range Between -2000 to 1000000000")
        if status =="":
            st.error("Select the Status")
        if item_type=="":
            st.error("Select the Item type")
        if application>=2 and application <=99:
            pass      
        else:
            st.error("Application Range Between 2 to 99")
        if thickness>=0.18 and thickness <=2500:
            pass
        else:
            st.error("Thickness Range Between 0.18 to 2500")
        if width>0 and width<2991:
            pass
        else:
            st.error("Width Range Between 1 to 2990")
        if country>=25 and country <=113:
            pass
        else:
            st.error("Country Range Between 25 to 113")
        if customer>=12458 and customer<=30408185:
            pass
        else:
            st.error("Customer Range Between 12458 to 30408185")
        if product_ref>=611728 and product_ref<=1722207579:
            pass
        else:
            st.error("Product Ref Range Between 611728 to 1722207579")                                                                       
        quantity_tons_log = np.log(quantity_tons)
        thickness_log=np.log(thickness)
        status_list=['Draft','Lost','Not lost for AM','Offerable','Offered','Revised','To be approved','Won','Wonderful']
        for number, statuses in enumerate(status_list):
            if status==statuses:
                status=number

        item_type_list=['IPL', 'Others', 'PL', 'S', 'SLAWR', 'W', 'WI']
        for number, items in enumerate(item_type_list):
            if item_type==items:
                item_type=number
        result=[[quantity_tons_log,status,item_type,application,thickness_log,width,country,customer,product_ref]]
        print(result)
        ss=joblib.load("ssreg.pkl")
        result_ss=ss.transform(result)
        print(result_ss)
        #st.write(result_ss)
        with open('rf_reg.pkl', 'rb') as file:
            rf = pickle.load(file)
        output=rf.predict(result_ss)
        Output=np.exp(output)
        st.title(Output[0])

if selected_option=='Classification':
    quantity_tons = st.text_input("Enter Quantity tons")
    selling_price =st.text_input("Enter Selling Price ")
    item_type=st.selectbox("Choose the Item type",("","IPL","Others","PL","S","SLAWR","W","WI"))
    application=st.number_input("Appication",min_value=2,max_value=99, value=2, step=1)
    thickness=st.text_input("Enter Thickness")
    #thickness=st.number_input("Thickness",min_value=0,max_value=2500, value=0, step=1)
    width=st.number_input("Width",min_value=1,max_value=2990, value=1, step=1)
    country=st.number_input("Country",min_value=25,max_value= 113, value=25, step=1)
    customer= st.number_input("Customer",min_value=12458,max_value= 30408185, value=12458, step=1)
    product_ref=st.number_input("Product Ref",min_value=611728,max_value= 1722207579, value=611728, step=1)
    predict=st.button("Predict")
    if predict:
        quantity_tons=float(quantity_tons)
        selling_price=float(selling_price)
        thickness=float(thickness)
        if quantity_tons >=-2000 and quantity_tons <=1000000000:
            pass
        else:
            st.error("Quantity Tons Range Between -2000 to 1000000000")
        if selling_price =="":
            st.error("Enter Your Selling Price")
        if item_type=="":
            st.error("Select the Item type")
        if application>=2 and application <=99:
            pass      
        else:
            st.error("Application Range Between 2 to 99")
        if thickness>=0.18 and thickness <=2500:
            pass
        else:
            st.error("Thickness Range Between 0.18 to 2500")
        if width>0 and width<2991:
            pass
        else:
            st.error("Width Range Between 1 to 2990")
        if country>=25 and country <=113:
            pass
        else:
            st.error("Country Range Between 25 to 113")
        if customer>=12458 and customer<=30408185:
            pass
        else:
            st.error("Customer Range Between 12458 to 30408185")
        if product_ref>=611728 and product_ref<=1722207579:
            pass
        else:
            st.error("Product Ref Range Between 611728 to 1722207579")                                                                       
        item_type_list=['IPL', 'Others', 'PL', 'S', 'SLAWR', 'W', 'WI']
        for number, items in enumerate(item_type_list):
            if item_type==items:
                item_type=number
        result=[[quantity_tons,selling_price,item_type,application,thickness,width,country,customer,product_ref]]
        print(result)
        ss=joblib.load("ssclas.pkl")
        result_ss=ss.transform(result)
        print(result_ss)
        #st.write(result_ss)
        with open('rf_clas.pkl', 'rb') as file:
            rf = pickle.load(file)
        output=rf.predict(result_ss)
        Output="Won" if output[0]==1 else "Loss"
        st.title(Output)
