"""
use if-elif-else statement
"""

number = input('Please input a number, we will check the number is positive, negative, or zero: ')
try:
    number = float(number)
    if number > 0:
        print('The number is positive.')
    elif number == 0:
        print('The number is zero.')
    else:
        print('The number is negative.')
except ValueError:
    print('The string you input can not transform to number.')

# use try-except statement to avoid transform data type error.