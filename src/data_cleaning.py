"""
Data Cleaning Script for Sales Dataset
This script loads messy sales data, applies cleaning transformations,
and outputs a clean CSV file ready for analysis.
"""


import pandas as pd


# Step 1: Load the raw data
# Purpose: Read the CSV file containing messy sales records
# Why: We need to load the data before we can clean it
# This file has inconsistent data formatting, missing values, and invalid entries
def load_data(file_path: str):
    """Load data from a CSV file and return as DataFrame"""


# Step 2: Standardize column names
# Purpose: Convert all column names to lowercase with underscores
# Why: Inconsistent column names (ex. "Product Name" vs "product_name")
# -cause errors when referencing columns. Standardizing prevents this.
def clean_column_names(df):
    """Standardize column names to lowercase with underscores"""


# Step 3: Handle missing values
# Purpose: Fill or remove rows with missing prices or quantities
# Why: Missing values in critical fields like price or quantity can skew analysis
# We will drop these rows to ensure all remaining data is useable.
def handle_missing_values(df):
    """Handle missing values in price and quantity columns"""


# Step 4: Remove invalid rows
# Purpose: Remove rows with negative prices or quantities
# Why: Negative values for price or quantity are invalid in sales data
def remove_invalid_rows(df):
    """Remove rows with invalid negative prices or quantities"""


# Step 5: Strip whitespace from text columns
# Purpose: Remove leading/trailing whitespace from text fields
# Why: "Laptop" and "laptop" should be treated as the same product.
# Whitespace causes duplicate categories and incorrect grouping.
def strip_whitespace(df):
    """Strip leading/trailing whitespace from text columns"""