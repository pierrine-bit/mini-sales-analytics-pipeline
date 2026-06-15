import pandas as pd


def extract_sales_data(file_path):
    """Load raw sales data from a CSV file into a DataFrame."""
    df = pd.read_csv(file_path)
    return df