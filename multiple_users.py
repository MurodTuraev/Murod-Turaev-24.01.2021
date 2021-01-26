import requests
import json
user = 10
response = requests.get(f'https://randomuser.me/api/?results={user}')
r = response.json()['results']
for i in r:
    name = i['name']['first']
    last = i['name']['last']
    full = name+' '+last+'\n'
    if response.status_code == 200:
        f = open('data.json', 'a')
        f.write(full)
    else:
        continue
