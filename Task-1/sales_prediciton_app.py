import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import pickle

# Load the trained XGBoost model
with open('xgb_model.pkl', 'rb') as file:
    xgb_model = pickle.load(file)

# Streamlit app
def main():
    # Custom favicon
    st.markdown(
        """
        <link rel="icon" href="data:,">
        <style>
            img {
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Custom CSS for styling
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }
            .main {
                max-width: 800px;
                margin: auto;
                padding: 20px;
            }
            h1 {
                color: #0066cc;
            }
            .btn-primary {
                background-color: #0066cc;
                color: #ffffff;
            }
            .btn-primary:hover {
                background-color: #0050a5;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Sales Prediction Web Application")

    # User inputs
    tv = st.text_input("TV Ad Spend", "")
    radio = st.text_input("Radio Ad Spend", "")
    newspaper = st.text_input("Newspaper Ad Spend", "")

    # Make a prediction on button click
    if st.button("Predict"):
        try:
            # Convert inputs to floats
            tv = float(tv)
            radio = float(radio)
            newspaper = float(newspaper)

            # Make a prediction using the XGBoost model
            prediction = xgb_model.predict([[tv, radio, newspaper]])

            st.success(f"Predicted Sales: {prediction[0]:.2f}")

        except ValueError:
            st.error("Please enter valid numerical values.")

if __name__ == '__main__':
    main()
