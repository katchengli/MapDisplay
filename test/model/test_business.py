'''
Created on Jul 4, 2016

@author: Katherine
'''
import unittest, json
from model.business import Business
from model.yelp_client import YelpClient

class TestBusiness(unittest.TestCase):


    def test_build__first_businesss_from_yelp_obj(self):
        yelpBusiness = YelpClient("../../yelp_auth.secret").fetchFirstBusiness()
        business = Business.buildFirstBusinessFromYelpObject(yelpBusiness)
        business = business.__dict__
        assert (business["businessName"] == "Blue Bottle Coffee Co")
    
    def test_return_JSON_of_businesses(self):
        business1 = Business("abc", "1", "2")
        business2 = Business("def", "3", "4")
        business3 = Business("ghi", "5", "6")
        listOfBusinesses = [business1, business2, business3]
        
        jsonOfBusinesses = Business.returnJSONOfBusinesses(listOfBusinesses)
        
        listOfBusinesses = json.loads(jsonOfBusinesses)
        
        assert (listOfBusinesses[1]["businessName"] == "def")
        
    def test_build_businessses_list_from_yelp_obj(self):
        yelpBusinesses = YelpClient("../../yelp_auth.secret").fetchCoffeeBusinesses()
        listOfBusinesses = Business.buildBusinessesListFromYelpObject(yelpBusinesses)
        
        assert (listOfBusinesses[0].businessName == "Blue Bottle Coffee Co")
    
    def test_get_businessses_list(self):
        listOfBusinesses = Business.getBusinessesList("../../yelp_auth.secret")
        
        assert (listOfBusinesses[0].businessName == "Blue Bottle Coffee Co")
        