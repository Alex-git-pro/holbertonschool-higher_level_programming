#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_case(self):
        """Test a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_with_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([10]), 10)

    def test_identical_elements(self):
        """Test a list with identical elements."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_elements(self):
        """Test a list with mixed positive, negative and zero values."""
        self.assertEqual(max_integer([3, -2, 0, 10, -5]), 10)

if __name__ == "__main__":
    unittest.main()
