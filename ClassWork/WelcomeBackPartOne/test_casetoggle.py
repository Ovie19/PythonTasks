import unittest
import casetoggle

class TestCaseToggle(unittest.TestCase):
    def test_that_toggle_case_function_gives_a_string_with_the_cases_of_the_character_toggled(self):
        word = "PyThOn"
        expected = casetoggle.toggle_case(word)
        actual = "pYtHoN"
        self.assertEqual(actual, expected)

        word = "BaBaLoLa"
        expected = casetoggle.toggle_case(word)
        actual = "bAbAlOlA"
        self.assertEqual(actual, expected)

        word = "ArSeNAl9"
        expected = casetoggle.toggle_case(word)
        actual = "aRsEnaL9"
        self.assertEqual(actual, expected)