import unittest
import currencyconverter

class TestCurrencyConverter(unittest.TestCase):

    def test_that_convert_currency_function_exists(self):
        currencyconverter.convert_currency(1)

    def test_that_convert_currency_function_return_correct_result(self):
        actual = currencyconverter.convert_currency(1)
        expected = 1550
        self.assertEqual(actual, expected)

        actual = currencyconverter.convert_currency(2.5)
        expected = 3875
        self.assertEqual(actual, expected)

        actual = currencyconverter.convert_currency(32)
        expected = 49600
        self.assertEqual(actual, expected)

#    def test_that_cube_function_return_invalid_data_type_with_wrong_input(self):
#        actual = functionplayground.cube("musa")
#        expected = "invalid input"
#        self.assertEqual(actual, expected)
#
#        actual = functionplayground.cube(True)
#        expected = "invalid input"
#        self.assertEqual(actual, expected)