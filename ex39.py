#create a mapping of state to abbreviation

states = {'Oregon': 'OR', 'Florida': 'FL', 'California':'CA', 'NewYork': 'NY', 'Michigan': 'MI'}

#create a basic set of states and some cities in them

cities = {'CA' : 'San Francisco', 'MI' : 'Detroit', 'FL' : 'Jacksonville', 'NY': 'NewJersey'}

#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities:

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("florida's abbreviation is: ",states['Florida'])

#do it by using the state then cities dict

print('-'*15)
print("Michigan has:", cities[states['Michigan']])
print("Floridas has:" , cities[states['Florida']])

#print every state abbr

print ('-'*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" %(state, abbrev))

#print evry city in state

print('-'*10)
for abbrev, city in cities.items():
    print("%s has the city %s"%(abbrev, city))

#now do both at the same time

print('-'*10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev]))

print('-'*10)

state = states.get('Texas', None)

if not state:
    print("sorry, no texas")

city = cities.get('TX', 'does not exist')
print("the city for the state 'TX' is: %s" %city)