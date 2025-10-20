import unittest
import os # test flake8
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    # add a test for subtract method
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)  

    # add a test for multi method
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(10, 5)
        self.assertEqual(result, 50)  

    # add test for divide method-float
    def test_divide_float(self):
        calc = Calculator()
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(10, 2), 5.0) # 10/2 也應是 5.0
        self.assertEqual(calc.divide(7, 4), 1.75)
    
    # add test for divide method-zero division
    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()