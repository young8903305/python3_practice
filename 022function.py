"""
function
"""

# get the initial alphabet of input name and turn into upper case
def get_initial(input_name):
    initial = input_name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_initial = get_initial(last_name)

print('Your initials are: ' + first_initial + last_initial)