import unittest
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
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

if __name__ == "__main__":
    unittest.main()