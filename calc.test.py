import unittest
from calc import calc

class TestCalc(unittest.TestCase):

def test_add_positive_integers(self):
    result = calc("+ 5 3")
    self.assertEqual(result, 8)
    pass

def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        calc("/ 5 0")


def test_modulo_negative_numbers(self):
    result = calc("% -15 4")
    self.assertEqual(result, 1)
if __name__ == "__main__":
    unittest.main()
