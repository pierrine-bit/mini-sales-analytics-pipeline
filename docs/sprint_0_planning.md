# Sprint 0 — Planning

## Product Vision

A lightweight ETL pipeline that reads raw sales CSV data, validates it, transforms it into clean and summarised outputs, and runs reliably in any environment.

## Product Backlog

| ID  | User Story | Priority | Story Points | Acceptance Criteria |
|-----|------------|----------|--------------|---------------------|
| US1 | As a data analyst, I want to load raw sales data from a CSV so that I can process it. | High | 1 SP | Given a valid CSV file exists, when the pipeline runs, then the data is loaded into a DataFrame without errors. |
| US2 | As a data analyst, I want automatic validation checks so that bad data is caught early. | High | 1 SP | Given data is loaded, when validation runs, then it raises an error for missing columns, null values, duplicate order IDs, or negative amounts. |
| US3 | As a data analyst, I want a cleaned sales output and a product summary so that I can analyse results. | High | 2 SP | Given validated data, when transformation runs, then `cleaned_sales.csv` and `sales_summary.csv` are written to the `data/` folder. |
| US4 | As a developer, I want automated unit tests so that changes do not break existing functionality. | Medium | 2 SP | Given the test suite, when `pytest tests/ -v` runs, then all tests pass with no failures. |
| US5 | As a developer, I want a CI pipeline so that tests run automatically on every push. | Medium | 1 SP | Given a push to `main`, when the GitHub Actions workflow triggers, then it installs dependencies and runs all tests automatically. |
| US6 | As a developer, I want Docker support so that the pipeline runs consistently in any environment. | Medium | 1 SP | Given a `Dockerfile` exists, when `docker build` and `docker run` are executed, then the pipeline runs and produces output without errors. |

## Definition of Done

A backlog item is considered complete when:

* Code is committed to the main branch.
* All unit tests pass.
* CI workflow runs green.
* Output files are produced without errors.

## Sprint 1 Plan

Stories selected based on highest priority and logical dependency order:

| ID  | User Story | Reason for Selection |
|-----|------------|----------------------|
| US1 | Load raw sales data from CSV | Foundation — no other step can run without data ingestion. |
| US2 | Add validation checks | Ensures data quality before any transformation happens. |
| US3 | Create cleaned sales output and product summary | Delivers the core end-to-end value of the pipeline. |

US4–US6 (testing, CI, Docker) are deferred to Sprint 2 once the core pipeline is verified working.
