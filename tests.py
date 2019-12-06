from santa import fuel_needed, original_fuel_needed
import unittest


class TestSanta(unittest.TestCase):

    def test_original_fuel_needed(self):
        self.assertEqual(original_fuel_needed(12),2)
        self.assertEqual(original_fuel_needed(14),2)
        self.assertEqual(original_fuel_needed(1969),654)
        self.assertEqual(original_fuel_needed(100756),33583)

    def test_fuel_needed(self):
        self.assertEqual(fuel_needed(14),2)
        self.assertEqual(fuel_needed(1969),966)
        self.assertEqual(fuel_needed(100756),50346)


if __name__ == '__main__':
    unittest.main()
