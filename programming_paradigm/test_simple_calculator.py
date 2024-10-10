import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,4), 10)
        self.assertEqual(self.calc.subtract(3,4), 0)
    
    def test_muliplication(self):
        self.assertEqual(self.calc.multiply(4,5), 9)
        self.assertEqual(self.calc.multiply(0,1), 10)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(4,6), 10)
        self.assertEqual(self.calc.divide(4, 1), 0)

# Remember to write additional test methods for subtract, multiply, and divide.
