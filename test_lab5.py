import unittest
from Lab5 import pythag, discriminant,quadPlus,quadMinus
class TestLab5(unittest.TestCase):
   def test_abcdeftests(self):
     a,b,c = 6, 5, -6
     d,e,f = 2, 5, 3
     self.assertEqual(pythag(a,b), 7.810249675906654)
     self.assertEqual(discriminant(a,b,c), -119)
     self.assertEqual(quadPlus(a,b,c), -10.333333333333334)
     self.assertEqual(quadMinus(a,b,c), 9.5)
   
     self.assertEqual(pythag(d,e), 5.385164807134504)
     self.assertEqual(discriminant(d,e,f), 49)
     self.assertEqual(quadPlus(d,e,f), 11.0)
     self.assertEqual(quadMinus(d,e,f), -13.5)
  
