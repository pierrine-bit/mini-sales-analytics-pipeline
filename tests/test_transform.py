import pandas as pd
from src.transform import clean_sales_data, create_sales_summary


# Shared sample data — amounts as strings to test type casting
def sample_df():
    return pd.DataFrame({
        "order_id": [101, 102, 103],
        "customer": ["Alice", "Bob", "Alice"],
        "product": ["Laptop", "Mouse", "Mouse"],
        "amount": ["1200", "40", "40"],
        "date": ["2026-05-01", "2026-05-02", "2026-05-03"],
    })


def test_clean_sales_data_casts_amount():
    cleaned = clean_sales_data(sample_df())
    assert cleaned["amount"].dtype == float


def test_clean_sales_data_casts_date():
    cleaned = clean_sales_data(sample_df())
    assert str(cleaned["date"].dtype) == "datetime64[ns]"


def test_clean_does_not_mutate_input():
    df = sample_df()
    clean_sales_data(df)
    assert df["amount"].dtype != float


def test_sales_summary_groups_by_product():
    cleaned = clean_sales_data(sample_df())
    summary = create_sales_summary(cleaned)
    assert set(summary["product"]) == {"Laptop", "Mouse"}


def test_sales_summary_totals():
    cleaned = clean_sales_data(sample_df())
    summary = create_sales_summary(cleaned)
    mouse_row = summary[summary["product"] == "Mouse"].iloc[0]
    assert mouse_row["total_sales"] == 80.0
    assert mouse_row["number_of_orders"] == 2


def test_sales_summary_sorted_descending():
    cleaned = clean_sales_data(sample_df())
    summary = create_sales_summary(cleaned)
    totals = list(summary["total_sales"])
    assert totals == sorted(totals, reverse=True)
