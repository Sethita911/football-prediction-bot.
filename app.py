import streamlit as st
import pandas as pd
from predictor import generate_prediction

st.set_page_config(page_title="Football Predictions", layout="wide")

st.title("Live Football Prediction Bot")
st.write("Predictions based on data from PredictZ, OneMillionPredictions, and BettingClosed.")

try:
    df = generate_prediction()
    st.success("Live data loaded from GitHub!")
    st.dataframe(df)
except Exception as e:
    st.error("Error loading predictions. Please check if the data file exists on GitHub.")
    st.code(str(e))
