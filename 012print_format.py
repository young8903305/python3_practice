"""
use four different ways about string concatenation, then print them out.
"""

first_name = 'Zeth'
last_name = 'Yang'

# string concatenation with +
output1 = 'Hello, ' + first_name + ' ' + last_name
print(output1)

# string concatenation with format function
output2 = 'Hello, {} {}'.format(first_name, last_name)
print(output2)

# string concatenation with format function and index, you can change the order of your parameters
output3 = 'Hello, {1} {0}'.format(first_name, last_name)
print(output3)

# string concatenation with "cool" format function 
output4 = f'Hello, {first_name} {last_name}'
print(output4)
