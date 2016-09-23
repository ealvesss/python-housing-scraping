#import requests
#r = requests.put('https://aarhus-housing.firebaseio.com/teste.json',data='{"arrived":1}')

#print r
#class Person(object):
##    def __init__(self, name, profession):
#        self.name = name
##        self.profession = profession
## 
#people = [Person("Nick", "Programmer"), Person("Alice","Engineer")]
#professions = dict([ (p.name, p.profession) for p in people ])
#print professions
#{"Nick": "Programmer", "Alice": "Engineer"}

#rikke toft noergaard 
#har du det godt?
#Jeg har det godt
#Jeg har det ikke godt


#learn how to say, why do you like games in danish

import json
response = []

response.append({'NOME': 'Elton'})

print json.dumps(response)