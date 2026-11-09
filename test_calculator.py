import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    #subtract()
    def test_subtract_normal(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    #multiply()
    def test_multiply_normal(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    #divide()
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    #modulo()
    def test_modulo_normal(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_exact(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

if __name__ == '__main__':
    unittest.main()