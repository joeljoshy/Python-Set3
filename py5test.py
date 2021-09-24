import unittest
from py5 import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(-1, 0)

        self.assertEqual(result1.addition(), 12)
        self.assertEqual(result2.addition(), -1)


    def test_sub(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(-1, 1)

        self.assertEqual(result1.subtraction(), 8)
        self.assertEqual(result2.subtraction(), -2)


    def test_mul(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(-1, 1)

        self.assertEqual(result1.multiplication(), 20)
        self.assertEqual(result2.multiplication(), -1)


    def test_div(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(10, 0)
        self.assertEqual(result1.division(), 5)


        with self.assertRaises(ValueError):
            result2.division()


if __name__ == '__main__':
    unittest.main()
