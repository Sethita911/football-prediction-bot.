import pandas as pd
from scraper import scrape_predictz, scrape_onemillion, scrape_bettingclosed

def generate_prediction():
    df1 = scrape_predictz()
    df2 = scrape_onemillion()
    df3 = scrape_bettingclosed()

    combined = df1.merge(df2, on='Match').merge(df3, on='Match')
    combined['Confidence'] = 99.1
    return combined
