"""
1. input function get user's input, always returns strings.
2. concern your data type when you calculate and print them.
"""

days_in_feb = 28
print(str(days_in_feb) + ' days in Feburary')

first_num = '5'
second_num = '6'
print(first_num + second_num)

# The input function always returns strings
first_num = input('Enter first nummber ')
second_num = input('Enter second nummber ')
print('first_num + second_number in string : ' + first_num + second_num)
print( f'the real calculation result: {int(first_num) ** int(second_num)}')

# This will add two numbers then print the result in float type
print(int(first_num) + float(second_num))
