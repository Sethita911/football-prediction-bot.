import streamlit as st
import pandas as pd
from predictor import generate_prediction

st.set_page_config(page_title="Football Prediction Bot", layout="wide")

st.title("Live Football Prediction Bot")
st.write("Predictions based on scraped data from trusted football tip sites.")

try:
    df = generate_prediction()
    st.success("Predictions loaded successfully!")
    st.dataframe(df)
except Exception as e:
    st.error("Error loading predictions. Please check if the predictions.csv file exists on GitHub and the URL is correct.")
    st.code(str(e))
