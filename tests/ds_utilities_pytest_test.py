import pandas as pd 
from my_lambdata.ds_utilities import enlarge, get_business_info

def test_enlarge():
    assert enlarge(3) == 300