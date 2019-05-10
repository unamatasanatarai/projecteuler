import unittest
from p0005 import smallest_multiple

class TestTask5(unittest.TestCase):
    def test_demo_data_works_well(self):
        self.assertEqual(smallest_multiple(1, 10), 2520)

if __name__ == "__main__":
    unittest.main()
