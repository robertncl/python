import unittest
from howler import main

class TestHowler(unittest.TestCase):

def test_main_empty_input(self):
    with unittest.mock.patch('sys.argv', ['howler.py', '']):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), '\n')
    pass

def test_main_special_chars_and_numbers(self):
    with unittest.mock.patch('sys.argv', ['howler.py', 'Hello123!@#']):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), 'HELLO123!@#\n')

if __name__ == '__main__':
    unittest.main()
