import argparse
from havinosh_data_loader import Config, Database, CSVProcessor
from havinosh_data_loader.logger import logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV to PostgreSQL ingestion script")
    parser.add_argument("--folder", type=str, default="csv_files", help="Folder containing CSV files")
    args = parser.parse_args()

    logger.info("🚀 Starting data ingestion...")

    # Load database configuration
    config = Config()
    db_config = config.get_config()

    # Create a database instance and connect
    db_instance = Database(db_config)
    db_instance.connect()

    # Initialize CSVProcessor with the database instance
    processor = CSVProcessor(db_instance, args.folder)
    
    # Process CSV files
    processor.process_csv()

    # Close database connection after processing
    db_instance.close()

    logger.info("✅ Data ingestion completed successfully!")
