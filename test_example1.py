import unittest
from Example1 import peremiter
class TestExample1(unittest.TestCase):

    def test_ints(self):
        self.assertEqual(peremiter(1,2),6)
        self.assertEqual(peremiter(2,4),12)
        self.assertEqual(peremiter(3,4),14)
        self.assertEqual(peremiter(100,200),600)
        self.assertEqual(peremiter(2,1),6)

if __name__ == '__main__':
    unittest.main()