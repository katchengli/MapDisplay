'''
Created on Jul 3, 2016

@author: Katherine
'''

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
    def buildFromYelpObject(cls, yelpBusiness):
        business = cls(yelpBusiness.name, yelpBusiness.location.coordinate.longitude, yelpBusiness.location.coordinate.latitude)
        
        return business.__dict__
        