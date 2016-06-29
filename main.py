'''
Created on Jun 28, 2016

@author: Katherine
'''
from model.yelp_client import YelpClient


if __name__ == '__main__':
    client = YelpClient("yelp_auth.secret")
    results = client.fetchBusinesses()
    print(results)