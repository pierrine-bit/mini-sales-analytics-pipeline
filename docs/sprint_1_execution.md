# Sprint 1 — Build Working Pipeline

## Sprint Goal

Deliver a working end-to-end pipeline that reads, validates, cleans, and saves sales data.

## Selected Stories

| ID  | User Story | Status |
|-----|------------|--------|
| US1 | Load raw sales data from CSV | Done |
| US2 | Add validation checks | Done |
| US3 | Create cleaned sales output and product summary | Done |

## Work Completed

* `extract.py` — reads raw CSV into a DataFrame
* `validate.py` — checks for required columns, nulls, duplicate IDs, and negative amounts
* `transform.py` — casts types, cleans data, and aggregates a product summary
* `load.py` — writes processed results to CSV
* `pipeline.py` — orchestrates all steps with structured logging

## Sprint Review

All three backlog items were delivered. The pipeline runs end-to-end, producing `cleaned_sales.csv` and `sales_summary.csv` in the `data/` folder.

## Sprint Retrospective

### What Went Well

* Modular structure made the code easy to follow and independently testable.
* Validation caught data quality issues before they could affect transformation.

### What to Improve in Sprint 2

* Add automated unit tests to catch regressions early.
* Configure CI to run tests automatically on every push.
* Add Docker support for consistent cross-environment execution.
