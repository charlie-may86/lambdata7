import unittest
import pandas as pd 
from my_lambdata.ds_utilities import enlarge

# To run the test
'''
python -m unittest tests/ds_utilities_assign_test.py
'''

class TestEnlarge(unittest.TestCase):

    def test_math(self):
        test = enlarge(3)
        self.assertEqual(test, 300)

if __name__ == '__main__':
    unittest.main()