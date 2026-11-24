import unittest
from services import calculate_fare

class TestRideServices(unittest.TestCase):
    def test_valid_fare(self):
        self.assertEqual(calculate_fare(10), 200.0)

    def test_invalid_distance(self):
        with self.assertRaises(ValueError):
            calculate_fare(-5)

if __name__ == "__main__":
    unittest.main()
