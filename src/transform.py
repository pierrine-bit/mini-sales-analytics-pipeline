def clean_sales_data(df):
    """Cast column types and return a cleaned copy without mutating the input."""
    df = df.copy()
    df["date"] = df["date"].astype("datetime64[ns]")
    df["amount"] = df["amount"].astype(float)
    return df


def create_sales_summary(df):
    """Aggregate total sales and order count per product, sorted descending."""
    summary = (
        df.groupby("product", as_index=False)
        .agg(
            total_sales=("amount", "sum"),
            number_of_orders=("order_id", "count")
        )
        .sort_values(by="total_sales", ascending=False)
    )
    return summary
