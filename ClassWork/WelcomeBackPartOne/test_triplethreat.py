import unittest
import triplethreat

class TestMultipleLetters(unittest.TestCase):
    def test_that_multiply_letters_function_gives_a_string_with_three_same_characters_in_a_row(self):
        word = "code"
        expected = triplethreat.multiply_letters(word)
        actual = "cccooodddeee"
        self.assertEqual(actual, expected)

        word = "EOB"
        expected = triplethreat.multiply_letters(word)
        actual = "EEEOOOBBB"
        self.assertEqual(actual, expected)

        word = "BaRcElOnA"
        expected = triplethreat.multiply_letters(word)
        actual = "BBBaaaRRRcccEEElllOOOnnnAAA"
        self.assertEqual(actual, expected)