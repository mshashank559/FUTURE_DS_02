import pandas as pd

def load_tickets(file_path):
    return pd.read_csv(file_path)
