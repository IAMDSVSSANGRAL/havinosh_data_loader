import unittest
from unittest.mock import MagicMock
import os
from havinosh_data_loader.process_csv import CSVProcessor
from havinosh_data_loader.db_utils import Database

class TestCSVProcessing(unittest.TestCase):
    """Unit tests for CSV processing"""

    def setUp(self):
        """Set up a mock database instance for testing"""
        self.mock_db = MagicMock(spec=Database)  # Mock the Database class
        self.test_csv_folder = "test_csvs"

        # Ensure test CSV folder exists
        os.makedirs(self.test_csv_folder, exist_ok=True)

        # Create a sample test CSV file
        sample_csv_path = os.path.join(self.test_csv_folder, "test_data.csv")
        with open(sample_csv_path, "w") as f:
            f.write("id,name,age\n1,John,30\n2,Jane,25")

        # Initialize CSV Processor with mock database
        self.processor = CSVProcessor(db_instance=self.mock_db, csv_folder=self.test_csv_folder)

    def test_process_csv(self):
        """Test CSV processing with a mock database"""
        self.processor.process_csv()  # Run CSV processing

        # Check if create_table and insert_data were called
        self.mock_db.create_table.assert_called()  # Ensure table creation is triggered
        self.mock_db.insert_data.assert_called()  # Ensure data insertion is triggered

    def tearDown(self):
        """Clean up after test"""
        for file in os.listdir(self.test_csv_folder):
            os.remove(os.path.join(self.test_csv_folder, file))
        os.rmdir(self.test_csv_folder)  # Remove test directory

if __name__ == "__main__":
    unittest.main()
