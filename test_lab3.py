import unittest
from Lab3 import area_triangle, prism_vol
class TestLab3(unittest.TestCase):
   def test_form_tests(self):
     self.assertEqual(area_triangle(6,6), 18.0)
     self.assertEqual(area_triangle(9,33), 148.5)
     self.assertEqual(area_triangle(10,11), 55.0)
     self.assertEqual(prism_vol(5,6,7), 210)
     self.assertEqual(prism_vol(11,11,11), 1331)
     self.assertEqual(prism_vol(2,9,4.5), 81.0)


        

if __name__ == '__main__':
    unittest.main()
  