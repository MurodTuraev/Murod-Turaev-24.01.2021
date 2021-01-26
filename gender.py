import requests
import json
gender = 'male'
results = 10
respose = requests.get(
    f'https://randomuser.me/api/?gender={gender}&results={results}')
r = respose.json()['results']
for i in r:
    name = i['name']['first']
    last = i['name']['last']
    fullname = name+' '+last
    gen = i['gender']
    data = fullname+' gender: '+gen+'\n'
    f = open('data.json', 'a')
    f.write(data)
