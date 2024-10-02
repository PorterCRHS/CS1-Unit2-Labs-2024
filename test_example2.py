import unittest
from example2 import area
class TestExample2(unittest.TestCase):

    def test_areasafsad(self):
        self.assertEqual(area(3, 3, 3),9.0)
        self.assertEqual(area(5, 6, 7),38.5)
        self.assertEqual(area(7, 10, 6),51.0)
        self.assertEqual(area(13, 19, 3),33)
        self.assertEqual(area(6, 11, 4),34.0)
        self.assertEqual(area(11, 8, 5),47.5)



        

if __name__ == '__main__':
    unittest.main()