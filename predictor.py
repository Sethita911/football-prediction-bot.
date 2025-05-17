import pandas as pd


def generate_prediction():
    url = "https://raw.githubusercontent.com/Sethita911/football-prediction-bot/main/predictions.csv"
    df = pd.read_csv(url)
    return df

