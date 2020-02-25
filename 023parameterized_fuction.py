"""
"""

# get the initial alphabet of input name and turn into upper case
def get_initial(input_name, force_uppercase=True):
    if force_uppercase:
        initial = input_name[0:1].upper()
    else:
        initial = input_name[0:1]
    return initial

# Ask for someone's first name and return the initials
first_name = input('Enter your first name: ')
first_initial = get_initial(force_uppercase=False, input_name=first_name)

# Ask for someone's last name and return the initials
last_name = input('Enter your last name: ')
last_initial = get_initial(last_name)

print('Your initials are: ' + first_initial + last_initial)
