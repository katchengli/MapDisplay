'''
Created on Jul 4, 2016

@author: Katherine
'''
import unittest
from model.business import Business
from model.yelp_client import YelpClient

class TestBusiness(unittest.TestCase):


    def test_build_from_yelp_obj(self):
        yelpBusiness = YelpClient("../../yelp_auth.secret").fetchFirstBusiness()
        business = Business.buildFromYelpObject(yelpBusiness)
        print(business)
        assert (business["businessName"] == "Blue Bottle Coffee Co")