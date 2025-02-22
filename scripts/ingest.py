import argparse
from loader.process_csv import process_csv
from loader.logger import logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV to PostgreSQL ingestion script")
    parser.add_argument("--folder", type=str, default="csv_files", help="Folder containing CSV files")
    args = parser.parse_args()

    logger.info("Starting data ingestion...")
    process_csv(args.folder)
    logger.info("Data ingestion completed successfully!")
