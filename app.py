import streamlit as st
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
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
    quantity_tons=st.number_input('Quantity Tons', min_value=-2000, max_value=1000000000, value=0, step=1)
    if quantity_tons and  quantity_tons >=-2000 and quantity_tons <=1000000000:
        st.write(quantity_tons)
        status= st.selectbox("Choose the Status",("","Draft","Lost","Not lost for AM","Offerable","Offered","Revised","To be approved","Won","Wonderful"))
        if status !="":
            item_type=st.selectbox("Choose the Item type",("","IPL","Others","PL","S","SLAWR","W","WI"))
            if item_type!="":
                application=st.number_input("Appication",min_value=2,max_value=99, value=2, step=1)
                if application and application>=2 and application <=99:
                    thickness=st.number_input("Thickness",min_value=0,max_value=2500, value=0, step=1)
                    if thickness and thickness>=0.18 and thickness <=2500:
                        width=st.number_input("Width",min_value=1,max_value=2990, value=1, step=1)
                        if width and width>0 and width<2991:
                            country=st.number_input("Country",min_value=25,max_value= 113, value=25, step=1)
                            if country and country>=25 and country <=113:
                                customer= st.number_input("Customer",min_value=12458,max_value= 30408185, value=12458, step=1)
                                if customer and customer>=12458 and customer<=30408185:
                                    product_ref=st.number_input("Product Ref",min_value=611728,max_value= 1722207579, value=611728, step=1)
                                    if product_ref and product_ref>=611728 and product_ref<=1722207579:
                                        predict=st.button("Predict")
                                        if predict:
                                            result=[quantity_tons,status,item_type,application,thickness,width,country,customer,product_ref]
                                            st.write(result)
                                            quantity_tons_log = np.log(quantity_tons)
                                            thickness_log=np.log(thickness)
                                            status=oe.fit_transform(status)
                                            item_type=oe.fit_transform(item_type)

if selected_option=='Classification':
    st.text_input("Quantity Tons")
