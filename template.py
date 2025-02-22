import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define project name
project_name = "loader"

# List of required files and folders
list_of_items = [
    f"{project_name}/__init__.py",
    f"{project_name}/config.py",
    f"{project_name}/process_csv.py",
    f"{project_name}/db_utils.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/utils.py",
    f"{project_name}/createtable.py",
    "scripts/ingest.py",
    "tests/test_process_csv.py",
    "csv_files/",
    "setup.py",
    ".env",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "LICENSE"
]

# Iterate through each path
for item in list_of_items:
    path = Path(item)

    # If item is a directory (ends with '/')
    if item.endswith("/"):
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"✅ Created directory: {path}")

    # If item is a file
    else:
        path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the parent directory exists
        if not path.exists():
            path.touch()  # Create an empty file
            logging.info(f"📄 Created file: {path}")
        else:
            logging.info(f"⚠️ File already exists: {path}")