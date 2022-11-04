import pandas as pd

def read_csv(io):
    return pd.read_csv(io)

def names(df):
    return df.columns.tolist()
