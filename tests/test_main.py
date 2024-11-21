import unittest
from src.main import get_terme, is_valid_input, is_palindrome

import datetime

class TestFunctions(unittest.TestCase):

    def test_get_terme_matin(self):
        now = datetime.datetime(2023, 10, 10, 9, 0, 0)
        self.assertEqual(get_terme(now), "Bonjour")

    def test_get_terme_aprem(self):
        now = datetime.datetime(2023, 10, 10, 15, 0, 0)
        self.assertEqual(get_terme(now), "Bonne après-midi")

    def test_get_terme_soir(self):
        now = datetime.datetime(2023, 10, 10, 20, 0, 0)
        self.assertEqual(get_terme(now), "Bonsoir")

    def test_is_valid_input_valid(self):
        self.assertTrue(is_valid_input("Bonjour"))
        self.assertTrue(is_palindrome("kayak"))

    def test_is_valid_input_invalid(self):
        self.assertFalse(is_valid_input("Bonjour123"))
        self.assertFalse(is_valid_input("Bonne après-midi!"))
        self.assertFalse(is_valid_input("*U*"))

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("kayak"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

if __name__ == '__main__':
    unittest.main()