import unittest
from p0007 import get_prime_number_at

class TestTask7(unittest.TestCase):
    def test_first_known_answers(self):
        self.assertEqual(get_prime_number_at(1), 2)
        self.assertEqual(get_prime_number_at(2), 3)
        self.assertEqual(get_prime_number_at(3), 5)
        self.assertEqual(get_prime_number_at(4), 7)
        self.assertEqual(get_prime_number_at(5), 11)
        self.assertEqual(get_prime_number_at(6), 13)
        self.assertEqual(get_prime_number_at(7), 17)

    def test_task_7(self):
        self.assertEqual(get_prime_number_at(10001), 104743)

if __name__ == "__main__":
    unittest.main()
