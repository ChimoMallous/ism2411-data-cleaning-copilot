"""
Data Cleaning Script for Sales Dataset
This script loads messy sales data, applies cleaning transformations,
and outputs a clean CSV file ready for analysis.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file and return as DataFrame"""
    return pd.read_csv(file_path)


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names to lowercase with underscores"""
    df = df.copy()
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values in price and quantity columns"""
    return df.copy().dropna(subset=['price', 'quantity'])


def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with invalid negative prices or quantities"""
    df = df.copy()
    return df[(df['price'] >= 0) & (df['quantity'] >= 0)]


def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading/trailing whitespace from text columns"""
    df = df.copy()
    string_cols = df.select_dtypes(include=['object']).columns
    df[string_cols] = df[string_cols].apply(lambda col: col.str.strip())
    return df
