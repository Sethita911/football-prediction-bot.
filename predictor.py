import pandas as pd
import pandas as pd

def generate_prediction():
    url = "https://raw.githubusercontent.com/Sethita911/football-prediction-bot/main/predictions.csv"
    df = pd.read_csv(url)
    return df
from scraper import scrape_predictz, scrape_onemillion, scrape_bettingclosed

def generate_prediction():
    df1 = scrape_predictz()
    df2 = scrape_onemillion()
    df3 = scrape_bettingclosed()

    combined = df1.merge(df2, on='Match').merge(df3, on='Match')
    combined['Confidence'] = 99.1
    return combined
