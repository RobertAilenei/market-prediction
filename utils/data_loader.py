import pandas as pd

def load_data(filepath):
    """Load and preprocess gold price data."""
    data = pd.read_csv(filepath, parse_dates=["Date"])
    data.sort_values("Date", inplace=True)
    return data
