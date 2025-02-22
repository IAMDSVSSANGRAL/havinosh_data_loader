import pandas as pd
import os
from loader.db_utils import create_table, insert_data
from loader.logger import logger
from loader.exception import LoaderException
import sys

def process_csv(csv_folder="csv_files"):
    """Read CSV files and insert into PostgreSQL dynamically"""
    try:
        for file in os.listdir(csv_folder):
            if file.endswith(".csv"):
                file_path = os.path.join(csv_folder, file)
                table_name = os.path.splitext(file)[0].lower()  # Use filename as table name
                
                df = pd.read_csv(file_path)
                logger.info(f"Processing file: {file}")

                create_table(table_name, df)
                insert_data(table_name, df)
                
                logger.info(f"Successfully ingested {file} into {table_name}")
    except Exception as e:
        raise LoaderException(e, sys)
