"""
example 2 of using if-elif-else statement

'or' in if condition
make a list to check different conditions but the same result
"""


country = input('What country do you live in? ')
tax = 0

if country.lower() == 'taiwan':    # case sensitive
    province = input('What province do you live in? ')
    if province.lower() == 'taipei' or province.lower() == 'new taipei':
        tax = 0.15
    elif province.lower() in ('taichung', 'tainan', 'hualian'):
        tax = 0.05
    else:
        tax = 0.03
else:
    tax = 0.0
print('Your tax is: ' + str(tax))


