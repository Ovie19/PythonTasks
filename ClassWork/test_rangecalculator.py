import unittest
import rangecalculator

class TestRangeCalculator(unittest.TestCase):
    def test_that_calculate_range_function_on_array_gives_valid_result(self):
        numbers = [2, 5, 7, 9, 20]
        expected = rangecalculator.calculate_range(numbers)
        actual = 18
        self.assertEqual(expected, actual)

        numbers = [2, 3, 1, 4, 6]
        expected = rangecalculator.calculate_range(numbers)
        actual = 5
        self.assertEqual(expected, actual)