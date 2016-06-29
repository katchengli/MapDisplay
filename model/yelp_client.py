'''
Created on Jun 28, 2016

@author: Katherine
'''
import json, io
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

class YelpClient(object):
    '''
    classdocs
    '''

    def __init__(self, yelp_auth_path):
        '''
        Constructor
        '''
        self.yelp_auth_path = yelp_auth_path
    
    def fetchBusinesses(self):  
        with io.open(self.yelp_auth_path) as auth_file:
            creds = json.load(auth_file)
            auth = Oauth1Authenticator(**creds)
            client = Client(auth)

        params = {
            'term': 'coffee',
            'lang': 'en'
        }
        
        coffee_shops = client.search('San Francisco', **params)
        return coffee_shops.businesses[0].name