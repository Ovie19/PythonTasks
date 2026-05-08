import unittest
import reoccuringnumbers

class TestReoccuringNumbers(unittest.TestCase):
    def test_that_get_reoccuring_numbers_function_on_array_gives_valid_result(self):
        numbers = [2, 1, 2, 5, 2, 4]
        expected = reoccuringnumbers.get_reoccuring_numbers(numbers)
        actual = [2]
        self.assertListEqual(expected, actual)

        numbers = [3, 4, 3, 4, 1, 5]
        expected = reoccuringnumbers.get_reoccuring_numbers(numbers)
        actual = [3, 4]
        self.assertListEqual(expected, actual)