import pandas as pd

def extract_csv(path: str) -> pd.DataFrame:
    print(f"Extracting data from {path}...")
    return pd.read_csv(path)
