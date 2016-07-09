'''
Created on Jun 28, 2016

@author: Katherine
'''
from model.yelp_client import YelpClient
from flask import Flask
from flask import jsonify
app = Flask(__name__)
    
@app.route('/')
def getCoffee():
    client = YelpClient("yelp_auth.secret")
    results = client.fetchCoffeeBusinesses()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)