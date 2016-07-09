'''
Created on Jun 28, 2016

@author: Katherine
'''
import unittest
from model.yelp_client import YelpClient

class TestYelpClient(unittest.TestCase):
    
    def test_fetch_first_business_name_integration(self):
        client = YelpClient("../../yelp_auth.secret")
        result = client.fetchFirstBusinessName()
        assert result == "Blue Bottle Coffee Co"