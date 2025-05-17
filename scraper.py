import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_predictz():
    url = "https://www.predictz.com/predictions/"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return pd.DataFrame([{'Match': 'Man Utd vs Chelsea', 'Prediction': 'Draw'}])

def scrape_onemillion():
    url = "https://onemillionpredictions.com/today-football-predictions/ht-ft-tips/"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return pd.DataFrame([{'Match': 'Man Utd vs Chelsea', 'HT/FT': '1/1'}])

def scrape_bettingclosed():
    url = "https://www.bettingclosed.com/predictions/date-matches/today/bet-type/correct-scores"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return pd.DataFrame([{'Match': 'Man Utd vs Chelsea', 'Score': '1-1'}])
