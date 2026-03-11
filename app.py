import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("car_price_model.pkl","rb"))
model_columns = pickle.load(open("model_columns.pkl","rb"))

st.title("Used Car Price Prediction")

present_price = st.number_input("Present Price")
kms_driven = st.number_input("Kms Driven")
owner = st.selectbox("Owner",[0,1,2,3])
car_age = st.number_input("Car Age")

fuel_type = st.selectbox("Fuel Type",["Petrol","Diesel","CNG"])
seller_type = st.selectbox("Seller Type",["Dealer","Individual"])
transmission = st.selectbox("Transmission",["Manual","Automatic"])

if st.button("Predict Price"):

    input_dict = {
        "Present_Price":present_price,
        "Kms_Driven":kms_driven,
        "Owner":owner,
        "Car_Age":car_age,
        "Fuel_Type_Diesel":1 if fuel_type=="Diesel" else 0,
        "Fuel_Type_Petrol":1 if fuel_type=="Petrol" else 0,
        "Seller_Type_Individual":1 if seller_type=="Individual" else 0,
        "Transmission_Manual":1 if transmission=="Manual" else 0
    }

    input_df = pd.DataFrame([input_dict])

    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)

    st.success(f"Predicted Price: {prediction[0]:.2f} Lakhs")