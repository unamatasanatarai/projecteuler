from lib import isDivisible, isEven
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

if __name__ == '__main__':
    unittest.main()
