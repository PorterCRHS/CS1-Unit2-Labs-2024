import unittest
from Lab2 import trick1, trick2
class TestExample2(unittest.TestCase):

    def test_areasafsad(self):
        self.assertEqual(trick1(5), 3.0)
        self.assertEqual(trick2(55), 15.0)
        self.assertEqual(trick1(2), 3.0)
        self.assertEqual(trick1(6), 3.0)
        self.assertEqual(trick1(8), 3.0)
        self.assertEqual(trick2(33), 15.0)
        self.assertEqual(trick2(69), 15.0)
        self.assertEqual(trick2(40), 15.0)


        

if __name__ == '__main__':
    unittest.main()