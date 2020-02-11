"""
comparing string in same case
"""

country = input('Enter the name of your home country: ')
# make sure your strings are in the same case before you compare them
# if country.upper() == 'CANADA':  <- this one also ok.
if country.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')