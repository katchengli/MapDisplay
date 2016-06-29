'''
Created on Jun 28, 2016

@author: Katherine
'''
import unittest
from model.yelp_client import YelpClient

class TestYelpClient(unittest.TestCase):
    
    def test_fetch_businesses_integration(self):
        client = YelpClient("../../yelp_auth.secret")
        result = client.fetchBusinesses()
        assert result == "Blue Bottle Coffee Co"