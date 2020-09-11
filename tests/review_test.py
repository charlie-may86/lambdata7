import unittest
from my_lambdata.review_class import Person

# to run in the python enviroment when importing from 
# another module
'''
python -m tests.review_test
'''

# to run the test
'''
python -m unittest tests/review_test.py
'''

class TestReview(unittest.TestCase):

    def test_age(self):
        charlie = Person('Charlie', 34, 'March', 'Nebraska')
        self.assertGreaterEqual(charlie.age, 0)
        self.assertLessEqual(charlie.age, 120)

if __name__ == '__main__':
    unittest.main()