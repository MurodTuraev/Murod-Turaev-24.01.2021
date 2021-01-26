import requests
import json
start_at = '2018-01-01'
end_at = '2018-01-03'
symbols = 'USD'
r = requests.get(
    f'https://api.exchangeratesapi.io/history?start_at={start_at}&end_at={end_at}&symbols={symbols}').json()
f = open('data.json', 'w')
f.write(str(r))
