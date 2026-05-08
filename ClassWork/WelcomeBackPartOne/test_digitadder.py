import unittest
import digitadder

class TestDigitAdder(unittest.TestCase):
    def test_that_digit_adder_function_gives_the_sum_of_digits_in_the_string(self):
        word = "a5b2c1"
        expected = digitadder.get_sum_in_string(word)
        actual = 8
        self.assertEqual(actual, expected)

        word = "12w453d8"
        expected = digitadder.get_sum_in_string(word)
        actual = 23
        self.assertEqual(actual, expected)