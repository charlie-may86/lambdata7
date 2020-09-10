import unittest
import pandas as pd 
from my_lambdata.ds_utilities import get_business_info

# To run the test
'''
python -m unittest tests/ds_utilities_test.py
'''

class TestDsUtilitiesMethods(unittest.TestCase):

    def test_upper(self):
        test_df = get_business_info('fast food', 'miami', 'state')
        self.assertGreaterEqual(len(test_df.iloc[0]['Phone_No']), 10)

if __name__ == '__main__':
    unittest.main()