"""
Introduce about list, dictionary, array
"""
from array import array

# an array example
# A new array whose items are restricted by typecode: double
scores = array('d')
scores.append(97)
scores.append(98)
scores.append(99)
print(scores)
print(scores[1])

# create a dict named bill
bill = {}
bill['first'] = 'Bill'
bill['last'] = 'Gates'

# create a dict named donald
donald = {}
donald['first'] = 'Donald'
donald['last'] = 'Trump'

# create a list named people
people = []
people.append(bill)    # append(): append object to the end of the list
people.append(donald)
people.append(24)    # you can add item into a list with different data types

print(bill)
print(donald)
print(people)
print('people[:1]: ' + str(people[:1]))


