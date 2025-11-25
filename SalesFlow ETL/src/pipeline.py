from extract import extract_csv
from transform import clean_sales
from load import load_to_sqlite
import pandas as pd

RAW_PATH = "data/raw/sales.csv"
PARQUET_PATH = "data/processed/cleaned_sales.parquet"
DB_PATH = "database/sales.db"

def run_pipeline():
    df = extract_csv(RAW_PATH)
    df_clean = clean_sales(df)

    # Save cleaned file
    df_clean.to_parquet(PARQUET_PATH)
    print(f"Saved cleaned file to {PARQUET_PATH}")

    # Load to database
    load_to_sqlite(df_clean, DB_PATH, "sales")
    print(f"Loaded data into database at {DB_PATH}")

if __name__ == "__main__":
    run_pipeline()
