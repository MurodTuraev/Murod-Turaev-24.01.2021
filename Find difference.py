import requests
import json
r1 = requests.get(
    'https://api.exchangeratesapi.io/2010-01-12').json()['rates']['RUB']
r2 = requests.get(
    'https://api.exchangeratesapi.io/latest').json()['rates']['RUB']
f = open('data.json', 'w')
f.write(str(r2-r1))
