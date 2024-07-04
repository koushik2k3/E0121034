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
        data = {
"companyName": "KPCompany",
"clientID": "afbac3d8-0a81-4c97-8031-bcb7bb3ea3ee",
"clientSecret": "ulfBXOzXtHabtjle",
"ownerName": "Koushik KP",
"ownerEmail": "koushikkp2003@gmail.com",
"accessCode": "JXUHXY",
"rollNo": "E0121034"
}
        response = requests.post('http://20.244.56.144/test/auth', json=data)
        token = response.json()['access_token']
        headers = {
'Authorization': f'Bearer {token}'
}
        response = requests.get(f'http://20.244.56.144/test/{noType}', headers=headers)
        numbers_list = response.json()['numbers']
        prevState = limitedQueue.printer()
        for i in numbers_list:
            limitedQueue.add(i)
        currState = limitedQueue.printer()

        output = {
        "numbers": numbers_list,
        "windowPrevState": prevState,
        "windowCurrState": limitedQueue.printer(),
        "avg": sum(currState) / len(currState) 
        }

        return output
    


api.add_resource(AverageCalulator, '/numbers/<string:numberid>')

if __name__ == '__main__':
    app.run(debug=True)
