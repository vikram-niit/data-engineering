import pandas as pd

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Drop rows with nulls
    df = df.dropna(subset=["date", "amount"])

    return df
