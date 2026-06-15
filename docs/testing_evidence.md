# Testing Evidence

## Test Framework

* Framework: Pytest
* Python version: 3.12.3
* Test files: `tests/test_validate.py`, `tests/test_transform.py`

## Test Files

### test_validate.py

Tests for `src/validate.py`:

* `test_valid_data_passes` — valid data passes without errors
* `test_missing_column_raises` — raises error when a required column is missing
* `test_null_values_raise` — raises error when null values are present
* `test_duplicate_order_ids_raise` — raises error on duplicate order IDs
* `test_negative_amount_raises` — raises error on negative sales amounts

### test_transform.py

Tests for `src/transform.py`:

* `test_clean_sales_data_casts_amount` — amount column is cast to float
* `test_clean_sales_data_casts_date` — date column is cast to datetime
* `test_clean_does_not_mutate_input` — original DataFrame is not modified
* `test_sales_summary_groups_by_product` — summary groups correctly by product
* `test_sales_summary_totals` — total sales values are correct
* `test_sales_summary_sorted_descending` — summary is sorted by total sales descending

## Test Results

Screenshot: `screenshots/pytest_results.png`
