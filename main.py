'''
Created on Jun 28, 2016

@author: Katherine
'''
from model.yelp_client import YelpClient
from flask import Flask
app = Flask(__name__)


if __name__ == '__main__':
    pass
    #print(results)

@app.route('/')
def getCoffee():
    client = YelpClient("yelp_auth.secret")
    results = client.fetchBusinesses()
    return results