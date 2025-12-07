# Sales Data Cleaning Project

Python script that cleans messy sales data by standardizing column names, removing invalid rows, and handling missing values.

## How to Run
```bash
pip install pandas
python src/data_cleaning.py
```

Cleaned data will be saved to `data/processed/sales_data_clean.csv`

## What It Does
- Converts column names to lowercase
- Removes rows with missing prices or quantities
- Removes invalid data (negative or zero values)
- Strips whitespace from text columns