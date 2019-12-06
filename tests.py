from santa import fuel_needed, original_fuel_needed
from intcode import process_opcode
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

class TestOpcode(unittest.TestCase):
    def test_opcode(self):
        self.assertEqual(process_opcode("1,0,0,0,99"), "2,0,0,0,99")
        self.assertEqual(process_opcode("2,3,0,3,99"), "2,3,0,6,99")
        self.assertEqual(process_opcode("2,4,4,5,99,0"), "2,4,4,5,99,9801")
        self.assertEqual(process_opcode("1,1,1,4,99,5,6,0,99"), "30,1,1,4,2,5,6,0,99")



if __name__ == '__main__':
    unittest.main()
