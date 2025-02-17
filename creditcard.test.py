import unittest
from creditcard import CreditCard

class TestCreditCard(unittest.TestCase):
    def setUp(self):
        pass

def test_validate_valid_card(self):
    valid_card = CreditCard("4388576018402626")
    self.assertEqual(valid_card.validate(), "Valid Card")

def test_validate_invalid_card(self):
    invalid_card = CreditCard("1234567890123456")
    self.assertEqual(invalid_card.validate(), "Invalid Card")

if __name__ == "__main__":
    unittest.main()
