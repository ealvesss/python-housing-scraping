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

#import json
#response = []

#response.append({'NOME': 'Elton'})

#print json.dumps(response)


class HousingModel(object):
	def __init__(self):
		self._title = None
		self._type = None


	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		self._title = value

	@title.deleter
	def title(self):
		del self._title


	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, value):
		self._type = value

	@type.deleter
	def type(self):
		del self._type

	def __json__(self):
        return {'name': self.title, 'age': self.type}

class MyClass(object):
    name = 'John'
    age = 30

    def __json__(self):
        return {'name': self.name, 'age': self.age}


import json


class MyEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that leverages an object's `__json__()` method,
    if available, to obtain its default JSON representation. 

    """
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)

print json.dumps(MyClass(), cls=MyEncoder)

