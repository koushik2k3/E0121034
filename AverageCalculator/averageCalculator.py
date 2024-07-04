from flask import Flask
from flask_restful import Resource, Api
import requests
from dataStructures import *

app = Flask(__name__)
api = Api(app)

limitedQueue = LimitedQueue(10)

class AverageCalulator(Resource):
    def get(self, numberid):
        if numberid == 'e':
            noType = 'even'
        elif numberid == 'p':
            noType = 'primes'
        elif numberid == 'f':
            noType = 'fibo'
        elif numberid == 'r':
            noType = 'rand'
        headers = {
'Authorization': 'Bearer <Token>'
}
        response = requests.get(f'http://20.244.56.144/test/{noType}', headers=headers)
        numbers = response.json()['numbers']
        prevState = limitedQueue.printer()
        for i in numbers:
            limitedQueue.add(i)
        currState = limitedQueue.printer()

        output = {
        "numbers": numbers,
        "windowPrevState": prevState,
        "windowCurrState": limitedQueue.printer(),
        "avg": sum(currState) / len(currState) 
        }

        return output
    

'''create a data structure with size 10 and that takes in values but ignores duplicates and when inserting if 
size is breached remove oldest element and add new element'''

api.add_resource(AverageCalulator, '/numbers/<string:numberid>')

if __name__ == '__main__':
    app.run(debug=True)
