### predictor.py
import pandas as pd

def generate_prediction():
    url = "https://github.com/Sethita911/football-prediction-bot./blob/main/predictions.csv"
    df = pd.read_csv(url)
    return df


