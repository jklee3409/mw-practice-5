import unittest
from main import FourBasicOpt

class FourBasicOptTest(unittest.TestCase):

    def setUp(self):
        self.calc = FourBasicOpt()

    # --- 덧셈 테스트 ---
    def test_add_positive(self):
        self.assertEqual(self.calc.add(100, 10), 110)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(100, -10), 90)

    # --- 뺄셈 테스트 ---
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(100, 10), 90)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(100, -10), 110)

    # --- 나눗셈 테스트 ---
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(100, 10), 10)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(100, 0), 0)

    # --- 곱셈 테스트 ---
    def test_multiply_large(self):
        self.assertEqual(self.calc.multiply(100, 10), 1000)

    def test_multiply_one(self):
        self.assertEqual(self.calc.multiply(100, 1), 100)

if __name__ == '__main__':
    unittest.main()
