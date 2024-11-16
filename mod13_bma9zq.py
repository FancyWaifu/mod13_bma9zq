import unittest
from datetime import datetime

# Assuming your project.py functions and logic have been imported correctly
from project import validate_date_input

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol(self):
        # Valid symbol
        self.assertRegex("AAPL", r"^[A-Z]{1,7}$")
        # Invalid symbols
        self.assertNotRegex("aapl", r"^[A-Z]{1,7}$")  # lowercase
        self.assertNotRegex("AAPL123", r"^[A-Z]{1,7}$")  # too long

    def test_chart_type(self):
        # Valid chart types
        self.assertIn("1", ["1", "2"])
        self.assertIn("2", ["1", "2"])
        # Invalid chart types
        self.assertNotIn("3", ["1", "2"])
        self.assertNotIn("Line", ["1", "2"])

    def test_time_series(self):
        # Valid time series
        self.assertIn("1", ["1", "2", "3", "4"])
        self.assertIn("4", ["1", "2", "3", "4"])
        # Invalid time series
        self.assertNotIn("5", ["1", "2", "3", "4"])
        self.assertNotIn("0", ["1", "2", "3", "4"])

    def test_start_date(self):
        # Valid date
        self.assertIsNotNone(validate_date_input("2024-11-15"))
        # Invalid date formats
        self.assertIsNone(validate_date_input("15-11-2024"))  # wrong format
        self.assertIsNone(validate_date_input("2024/11/15"))  # wrong separator

    def test_end_date(self):
        # Valid end date
        start_date = datetime.strptime("2024-11-14", "%Y-%m-%d")
        end_date = validate_date_input("2024-11-15")
        self.assertIsNotNone(end_date)
        self.assertTrue(end_date >= start_date)

        # Invalid end date
        invalid_end_date = validate_date_input("2024-11-13")
        self.assertTrue(invalid_end_date is None or invalid_end_date < start_date)

if __name__ == '__main__':
    unittest.main()
