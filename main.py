'''
Created on Jun 28, 2016

@author: Katherine
'''
from model.business import Business
from flask import Flask
from flask.helpers import send_from_directory
app = Flask(__name__)

@app.route('/map')
def mapDisplay():
    #results = Business.getBusinessesList()
    #return results
    return send_from_directory('view', 'map.html')

@app.route('/coffeedata')
def getCoffeeBusinesses():
    results = Business.getBusinessesList()
    return results

if __name__ == '__main__':
    app.run(debug=True)