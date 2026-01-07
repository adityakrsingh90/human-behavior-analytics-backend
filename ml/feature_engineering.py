import pandas as pd

def create_features(df):
    df["sleep_debt"] = 8 - df["sleep_hours"]
    df["focus_ratio"] = df["focus_sessions"] / (df["screen_time"] + 1)
    return df
