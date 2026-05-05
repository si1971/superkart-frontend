import streamlit as st
import requests

st.set_page_config(page_title="SuperKart Sales Predictor", layout="centered")

st.title("SuperKart Sales Revenue Prediction")
st.write("Enter product and store details to forecast product-store sales revenue.")

# Backend API URL
API_URL = "https://shibuittoop-superkart-backend-api.hf.space/predict"
# If your backend URL is different, replace the above URL with the correct one.

Product_Id = st.text_input("Product ID", "FDX07")

Product_Weight = st.number_input(
    "Product Weight",
    min_value=0.0,
    value=19.2
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    value=0.067
)

Product_Type = st.selectbox(
    "Product Type",
    [
        "Fruits and Vegetables",
        "Snack Foods",
        "Frozen Foods",
        "Dairy",
        "Household",
        "Baking Goods",
        "Canned",
        "Health and Hygiene",
        "Meat",
        "Soft Drinks",
        "Breads",
        "Hard Drinks",
        "Others",
        "Starchy Foods",
        "Breakfast",
        "Seafood",
    ],
)

Product_MRP = st.number_input(
    "Product MRP",
    min_value=0.0,
    value=249.8
)

Store_Id = st.selectbox(
    "Store ID",
    ["OUT001", "OUT002", "OUT003", "OUT004"]
)

Store_Establishment_Year = st.number_input(
    "Store Establishment Year",
    min_value=1900,
    max_value=2026,
    value=1999
)

Store_Size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Supermarket Type1",
        "Supermarket Type2",
        "Food Mart",
    ],
)

if st.button("Predict Sales"):
    input_data = {
        "Product_Id": Product_Id,
        "Product_Weight": Product_Weight,
        "Product_Sugar_Content": Product_Sugar_Content,
        "Product_Allocated_Area": Product_Allocated_Area,
        "Product_Type": Product_Type,
        "Product_MRP": Product_MRP,
        "Store_Id": Store_Id,
        "Store_Establishment_Year": Store_Establishment_Year,
        "Store_Size": Store_Size,
        "Store_Location_City_Type": Store_Location_City_Type,
        "Store_Type": Store_Type,
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()

            if "predicted_Product_Store_Sales_Total" in result:
                prediction = result["predicted_Product_Store_Sales_Total"]
                st.success(f"Predicted Sales Revenue: {prediction:,.2f}")
            else:
                st.error(f"Unexpected API response: {result}")

        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"Connection error: {e}")
