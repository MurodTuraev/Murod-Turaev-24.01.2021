import requests
import json
r = requests.get(
    'https://api.exchangeratesapi.io/latest?symbols=USD,GBP').json()
f = open('data.json', 'w')
f.write(str(r))
