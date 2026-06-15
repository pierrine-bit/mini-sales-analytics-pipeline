import logging

from src.extract import extract_sales_data
from src.validate import validate_sales_data
from src.transform import clean_sales_data, create_sales_summary
from src.load import load_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


RAW_DATA_PATH = "data/raw_sales.csv"
CLEANED_DATA_PATH = "data/cleaned_sales.csv"
SUMMARY_DATA_PATH = "data/sales_summary.csv"


def run_pipeline():
    logger.info("Starting sales pipeline")

    try:
        raw_data = extract_sales_data(RAW_DATA_PATH)
        logger.info("Raw sales data extracted successfully")

        validate_sales_data(raw_data)
        logger.info("Data validation completed successfully")

        cleaned_data = clean_sales_data(raw_data)
        logger.info("Data cleaning completed successfully")

        sales_summary = create_sales_summary(cleaned_data)
        logger.info("Sales summary created successfully")

        load_data(cleaned_data, CLEANED_DATA_PATH)
        load_data(sales_summary, SUMMARY_DATA_PATH)

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()