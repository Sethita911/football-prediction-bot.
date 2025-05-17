### predictor.py
import pandas as pd

def generate_prediction():
    url = "predictions.csv"
    df = pd.read_csv(url)
    return df


