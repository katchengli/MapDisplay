import json, io
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from pprint import pprint

with io.open('../yelp_auth.secret') as auth_file:
    creds = json.load(auth_file)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
    'term': 'coffee',
    'lang': 'en'
}

coffee_shops = client.search('San Francisco', **params)
pprint(coffee_shops.businesses[0].name)

