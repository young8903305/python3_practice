"""
judge the year is leap year or not

"""

while 1:
    year = int(input('type year to check leap year or not: '))
    if year % 400 or year % 4 == 0 and year % 100 != 0:
        print('yes')
    else:
        print('not')
