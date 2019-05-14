from lib import is_divisible, is_even, is_prime, is_palindrome, prime_sieve
import unittest

class TestLibrary(unittest.TestCase):
    def test_is_divisible(self):
        by3 = is_divisible(3)
        self.assertTrue(by3(6))
        self.assertTrue(by3(9))
        self.assertTrue(by3(12))
        self.assertTrue(by3(15))
        self.assertFalse(by3(13))

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(8))
        self.assertFalse(is_even(1))

    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(47))
        self.assertFalse(is_prime(46))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))

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

    def test_prime_sieve(self):
        self.assertEqual(sum(prime_sieve(21)), 77)
        self.assertEqual(sum(prime_sieve(2000000)), 142913828922)

if __name__ == '__main__':
    unittest.main()
