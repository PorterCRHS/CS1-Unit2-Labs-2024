import unittest
from Lab4 import f_to_c, c_to_f
class TestLab4(unittest.TestCase):
   def test_temp_tests(self):
     self.assertEqual(f_to_c(32), 0.0)
     self.assertEqual(c_to_f(0), 32.0)
     self.assertEqual(f_to_c(212), 100.0)
     self.assertEqual(c_to_f(100), 212.0)
     self.assertEqual(f_to_c(50), 10.0)
     self.assertEqual(c_to_f(10), 50.0)
   

        

if __name__ == '__main__':
    unittest.main()
  