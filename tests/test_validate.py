import pytest
import pandas as pd
from src.validate import validate_sales_data


# Base factory — overrides allow individual tests to inject invalid data
def make_df(**overrides):
    base = {
        "order_id": [1, 2],
        "customer": ["Alice", "Bob"],
        "product": ["Laptop", "Mouse"],
        "amount": [1200.0, 40.0],
        "date": ["2026-05-01", "2026-05-02"],
    }
    base.update(overrides)
    return pd.DataFrame(base)


def test_valid_data_passes():
    assert validate_sales_data(make_df()) is True


def test_missing_column_raises():
    df = make_df()
    df = df.drop(columns=["amount"])
    with pytest.raises(ValueError, match="Missing required column: amount"):
        validate_sales_data(df)


def test_null_values_raise():
    df = make_df()
    df.loc[0, "customer"] = None
    with pytest.raises(ValueError, match="missing values"):
        validate_sales_data(df)


def test_duplicate_order_ids_raise():
    df = make_df(order_id=[1, 1])
    with pytest.raises(ValueError, match="duplicate order IDs"):
        validate_sales_data(df)


def test_negative_amount_raises():
    df = make_df(amount=[-10.0, 40.0])
    with pytest.raises(ValueError, match="negative sales amounts"):
        validate_sales_data(df)
