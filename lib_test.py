from lib import isDivisible, isEven, isPrime
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
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(47))
        self.assertFalse(isPrime(46))
        self.assertFalse(isPrime(0))
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(-1))

if __name__ == '__main__':
    unittest.main()
