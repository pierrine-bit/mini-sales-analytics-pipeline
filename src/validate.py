def validate_sales_data(df):
    """Check data quality before transformation. Raises ValueError on any violation."""
    required_columns = ["order_id", "customer", "product", "amount", "date"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Data contains missing values")

    if df["order_id"].duplicated().any():
        raise ValueError("Data contains duplicate order IDs")

    if (df["amount"] < 0).any():
        raise ValueError("Data contains negative sales amounts")

    return True
