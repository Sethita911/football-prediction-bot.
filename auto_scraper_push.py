import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from github import Github

# TODO: Replace this with your GitHub token
GITHUB_TOKEN = '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'
REPO_NAME = 'Sethita911/football-prediction-bot'
FILE_PATH = 'predictions.csv'

def scrape_predictz():
    # Dummy example – replace with real scraper
    return pd.DataFrame([{'Match': 'Man Utd vs Chelsea', 'Prediction': 'Draw'}])

def scrape_onemillion():
    return pd.DataFrame([{'Match': 'Man Utd vs Chelsea', 'HT/FT': '1/1'}])

def scrape_bettingclosed():
    return pd.DataFrame([{'Match': 'Man Utd vs Chelsea', 'Score': '1-1'}])

def save_and_push(df):
    df['Updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    df.to_csv("predictions.csv", index=False)

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    try:
        contents = repo.get_contents(FILE_PATH)
        repo.update_file(contents.path, "Update predictions", df.to_csv(index=False), contents.sha)
    except:
        repo.create_file(FILE_PATH, "Create predictions", df.to_csv(index=False))

df1 = scrape_predictz()
df2 = scrape_onemillion()
df3 = scrape_bettingclosed()

combined = df1.merge(df2, on='Match').merge(df3, on='Match')
combined['Confidence'] = 99.2

save_and_push(combined)
print("Data scraped and pushed to GitHub.")
