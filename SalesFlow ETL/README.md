# Simple Data Engineering ETL Project

This project demonstrates a basic **ETL (Extract, Transform, Load)** pipeline using Python.
The pipeline reads raw CSV data, cleans it, converts it to Parquet, and loads it into a SQLite database.

---

## 🏗 Project Structure
```bash
data-engineering-project/
│
├── data/
│   ├── raw/                # Place raw CSVs here
│   └── processed/          # Output Parquet files
│
├── src/
│   ├── extract.py          # Extracts data
│   ├── transform.py        # Cleans and transforms data
│   ├── load.py             # Loads into SQLite
│   └── pipeline.py         # Orchestrates ETL job
│
├── database/               # SQLite DB lives here
├── requirements.txt
└── README.md
```
---

## 🧪 Input Data Format

The CSV file must have the columns:

- date (e.g., "2024-01-01")
- amount (numeric)

Example:

date,amount
2024-01-01,100
2024-01-01,200
2024-01-02,300


---

## 🛠 Setup & Installation

### 1. Clone the project

git clone <your-repo>
cd data-engineering-project

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add raw CSV file
Place your CSV file at:
data/raw/sales.csv

---

## ▶️ Running the Pipeline
python src/pipeline.py

This will:

1. Read `data/raw/sales.csv`
2. Clean data (type conversions, remove nulls)
3. Save processed data to Parquet:
   data/processed/cleaned_sales.parquet
4. Create SQLite DB at:
  database/sales.db
5. Load:
- `sales` table
- `daily_summary` table (aggregated totals)

---

## 📊 Verifying the Output

### View tables in SQLite:
```bash
sqlite3 database/sales.db
sqlite> .tables
sqlite> SELECT * FROM daily_summary;
```

---

## 🚀 Deployment Options

You can deploy the pipeline using:

### **Option A: Cron (Linux)**
Edit crontab:
crontab -e

Add to run daily at 2 AM:
0 2 * * * python /path/to/pipeline.py


### **Option B: Airflow**

Create a DAG that calls `pipeline.py`.

### **Option C: Docker**

1. Create a Dockerfile (optional)
2. Run pipeline inside container

---

## ✔️ End of README
