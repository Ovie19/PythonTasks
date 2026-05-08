import unittest
import spacecompressor

class TestSpaceCompressor(unittest.TestCase):
    def test_that_compress_space_function_gives_a_string_with_the_space_converted_to_hyphen(self):
        word = "Hello World !"
        expected = spacecompressor.compress_space(word)
        actual = "Hello-World-!"
        self.assertEqual(actual, expected)

        word = "Emmanuel Babalola"
        expected = spacecompressor.compress_space(word)
        actual = "Emmanuel-Babalola"
        self.assertEqual(actual, expected)

        word = "Arsenal The Bottlers"
        expected = spacecompressor.compress_space(word)
        actual = "Arsenal-The-Bottlers"
        self.assertEqual(actual, expected)