import requests
import json
national = 'IE'
gender = 'male'
results = 10
response = requests.get(
    f'https://randomuser.me/api/?nat={national}&results={results}&gender={gender}')
r = response.json()['results']
for i in r:
    name = i['name']['first']
    last = i['name']['last']
    fullname = name+' '+last
    gen = i['gender']
    nat = i['nat']
    data = fullname+', ' + 'gender is: '+gen+', '+' Nationalities is: '+nat+'\n'
    f = open('data.json', 'a')
    f.write(data)
