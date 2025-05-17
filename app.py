import streamlit as st
from predictor import generate_prediction

st.title("AI Football Prediction Bot")
st.markdown("**Data Sources**: Predictz, OneMillionPredictions, BettingClosed")

df = generate_prediction()
st.dataframe(df)
