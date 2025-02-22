# __init__.py: Marks the directory as a package
from .config import DB_CONFIG
from .db_utils import create_table, insert_data
from .process_csv import process_csv
