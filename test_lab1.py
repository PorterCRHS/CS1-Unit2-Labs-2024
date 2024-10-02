import unittest
from unittest.mock import patch

import io
import contextlib
from Lab1 import happy_birthday
class TestLab1(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_outputSecret(self, mock_stdout):
        happy_birthday("a secret person")
        self.assertEqual(mock_stdout.getvalue().strip(), "Happy birthday, a secret person!")
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_outputSecret(self, mock_stdout):
        happy_birthday("mom")
        self.assertEqual(mock_stdout.getvalue().strip(), "Happy birthday, mom!")

if __name__ == '__main__':
    unittest.main()

