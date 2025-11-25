import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Create a summary table
    summary = df.groupby(df["date"].dt.date)["amount"].sum().reset_index()
    summary.to_sql("daily_summary", conn, if_exists="replace", index=False)

    conn.close()
