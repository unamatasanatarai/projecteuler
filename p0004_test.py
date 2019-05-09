import unittest
from p0004 import is_palindrome

class TestTask4(unittest.TestCase):
    def test_is_palindrome_from_numbers(self):
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(123321))
        self.assertTrue(is_palindrome(12321))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("1"))
        self.assertTrue(is_palindrome("11"))
        self.assertTrue(is_palindrome("112211"))
        self.assertTrue(is_palindrome("112abba211"))
        self.assertTrue(is_palindrome("kayak"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("aya"))

    def test_is_not_palindrome(self):
        self.assertFalse(is_palindrome("27"))
        self.assertFalse(is_palindrome("274"))
        self.assertFalse(is_palindrome("robot"))

if __name__ == "__main__":
    unittest.main()
