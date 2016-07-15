'''
Created on Jul 3, 2016

@author: Katherine
'''

import json
from model.yelp_client import YelpClient

class Business(object):
    '''
    classdocs
    '''

    def __init__(self, businessName, longit, latit):
        '''
        Constructor
        '''
        self.businessName = businessName
        self.longitude = longit
        self.lattitude = latit
        
    @classmethod
    def buildFirstBusinessFromYelpObject(cls, yelpBusiness):
        business = cls(yelpBusiness.name, yelpBusiness.location.coordinate.longitude, yelpBusiness.location.coordinate.latitude)
        
        return business
        
    @classmethod
    def returnJSONOfBusinesses(cls, listOfBusinesses):
        
        return json.dumps([business.__dict__ for business in listOfBusinesses])
    
    @classmethod
    def buildBusinessesListFromYelpObject(cls, yelpBusinesses):
        
        listOfBusinesses = list(cls(yelpBusiness.name, yelpBusiness.location.coordinate.longitude, yelpBusiness.location.coordinate.latitude) for yelpBusiness in yelpBusinesses)
        
        return listOfBusinesses
    
    @classmethod
    def getBusinessesList(cls, yelp_config_path = None):
        yelpClient = YelpClient(yelp_config_path or "./yelp_auth.secret")
        yelpCoffeeBusinesses = yelpClient.fetchCoffeeBusinesses()
        businessList = Business.buildBusinessesListFromYelpObject(yelpCoffeeBusinesses)
        
        return Business.returnJSONOfBusinesses(businessList)
        
        
        