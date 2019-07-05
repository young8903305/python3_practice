"""
judge the year is leap year or not

"""

while 1:
    year = (input('type year to check leap year or not: '))
    if str.isdigit(year):
        year = int(year)
        if year % 400 or year % 4 == 0 and year % 100 != 0:
            print('yes')
        else:
            print('not')
    else:
        print('please type in a number')
