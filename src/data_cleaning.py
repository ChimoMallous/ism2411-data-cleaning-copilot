"""
Data Cleaning Script for Sales Dataset
This script loads messy sales data, applies cleaning transformations,
and outputs a clean CSV file ready for analysis.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file and return as DataFrame"""
    # MODIFIED: Added error handling that Copilot didn't include
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise



def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names to lowercase with underscores"""
    # MODIFIED: Add strip leading/trailing spaces before converting to lowercase, Add lowercase formating for 'prodname' and 'category' columns
    df = df.copy()
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    if 'prodname' in df.columns:
        df['prodname'] = df['prodname'].str.lower()
    if 'category' in df.columns:
        df['category'] = df['category'].str.lower()

    return df

# MODIFIED: Added function to convert price and qty to numeric types
def convert_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values in price and quantity columns"""
    # MODIFIED: Added print statement to track how many rows were dropped
    df = df.copy()
    rows_before = len(df)
    df = df.dropna(subset=['price', 'qty'])
    print(f"Dropped {rows_before - len(df)} rows due to missing values.")
    return df


def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with invalid negative prices or quantities"""
    df = df.copy()
    # MODIFIED: Instead of removing rows with negative values as GitHub Copilot suggested,
    # -we now replace those values with their absolute value
    df['price'] = df['price'].abs()
    df['qty'] = df['qty'].abs()
    return df

def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading/trailing whitespace from text columns"""
    df = df.copy()
    string_cols = df.select_dtypes(include=['object']).columns
    df[string_cols] = df[string_cols].apply(lambda col: col.str.strip())

    # MODIFIED: Add strip leading and trailing whitespace from columns, remove quotation marks
    df['prodname'] = df['prodname'].str.replace('"', '').str.strip()
    df['category'] = df['category'].str.replace('"', '').str.strip()
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    print("RAW COLUMNS:", df_raw.columns.tolist())   
    print(df_raw.head()) 

    df_clean = clean_column_names(df_raw)
    df_clean = strip_whitespace(df_clean)
    df_clean = convert_to_numeric(df_clean)   
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())