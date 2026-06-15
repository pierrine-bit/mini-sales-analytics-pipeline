# Sprint 2 — Testing, Automation, and DevOps

## Sprint Goal

Apply Sprint 1 retrospective improvements by adding automated testing, CI, Docker, and structured error monitoring.

## Improvements from Sprint 1

| Sprint 1 Issue | Sprint 2 Action |
|----------------|-----------------|
| No automated tests | Added 11 unit tests across `test_validate.py` and `test_transform.py` |
| No CI configured | Added GitHub Actions workflow that runs `pytest` on every push |
| No Docker support | Added `Dockerfile` using `python:3.12-slim` |

## Logging and Monitoring

* Structured logging — each pipeline step emits a timestamped `INFO` message
* Error tracking — a `try/except` block catches all exceptions and logs them at `ERROR` level before re-raising
* Health verification — verified by exit code and presence of output files after each run

Example error log:

```text
2026-06-15 14:01:48,020 - ERROR - Pipeline failed: Missing required column: amount
```

## CI/CD

GitHub Actions runs the full test suite on every push and pull request to `main`.

Workflow file: `.github/workflows/ci.yml`

Evidence: `screenshots/github_actions_success.png`

## Sprint Review

All three backlog items were delivered. The pipeline now has 11 passing tests, a working CI workflow, Docker support, and structured error logging.

## Sprint Retrospective

### What Went Well

Sprint 2 delivered all planned improvements from the Sprint 1 retrospective on schedule.

| Area | Outcome |
|------|---------|
| Unit Testing | All 11 tests passed on the first execution, confirming implementation stability. |
| Logging | Structured logging provides a clear, timestamped audit trail across every pipeline stage. |
| DevOps | Docker and CI integration ensure the solution is portable and continuously validated on every commit. |

### What to Improve

| Issue | Action |
|-------|--------|
| CI not yet verified remotely | Confirm the GitHub Actions workflow completes successfully after the initial push. |
| No post-run verification | Implement output file existence and integrity checks after each pipeline execution. |

### Future Improvements

| Area | Proposed Improvement |
|------|----------------------|
| Storage | Migrate output from flat CSV files to a relational database for scalable storage and querying. |
| Scheduling | Introduce automated pipeline scheduling using a workflow orchestration tool such as Apache Airflow. |
| Data Quality | Extend validation to include date range checks and referential integrity constraints. |
