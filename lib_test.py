from lib import isDivisible, isEven, is_prime
import unittest

class TestLibrary(unittest.TestCase):
    def test_is_divisible(self):
        by3 = isDivisible(3)
        self.assertTrue(by3(6))
        self.assertTrue(by3(9))
        self.assertTrue(by3(12))
        self.assertTrue(by3(15))
        self.assertFalse(by3(13))

    def test_is_even(self):
        self.assertTrue(isEven(2))
        self.assertTrue(isEven(4))
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(1))

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

if __name__ == '__main__':
    unittest.main()
