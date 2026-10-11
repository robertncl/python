import io
import unittest
from unittest import mock

from howler import main


class TestHowler(unittest.TestCase):

    def test_main_empty_input(self):
        with mock.patch('sys.argv', ['howler.py', '']), \
                mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), '\n')

    def test_main_special_chars_and_numbers(self):
        with mock.patch('sys.argv', ['howler.py', 'Hello123!@#']), \
                mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), 'HELLO123!@#\n')


if __name__ == '__main__':
    unittest.main()
