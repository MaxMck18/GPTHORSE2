# scripts/scrape_data.py

import pandas as pd
from datetime import datetime
import os

def scrape_data():
    # Simulate some mock Australian race data for today
    races = [
        {"race_id": "AUS001", "horse": "Thunderbolt", "form": 2, "odds": 3.5, "jockey_rating": 85, "track": "Good"},
        {"race_id": "AUS001", "horse": "Fast Flash", "form": 1, "odds": 5.0, "jockey_rating": 80, "track": "Good"},
        {"race_id": "AUS001", "horse": "Sky Rocket", "form": 3, "odds": 4.5, "jockey_rating": 78, "track": "Good"},
        {"race_id": "AUS002", "horse": "Golden Speed", "form": 1, "odds": 2.5, "jockey_rating": 92, "track": "Soft"},
        {"race_id": "AUS002", "horse": "Iron Hoof", "form": 4, "odds": 6.0, "jockey_rating": 75, "track": "Soft"},
        {"race_id": "AUS002", "horse": "Quick Snap", "form": 2, "odds": 3.8, "jockey_rating": 83, "track": "Soft"},
    ]

    df = pd.DataFrame(races)
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/today_races.csv", index=False)
    return df
