"""
datetime object, strptime() example
"""
from datetime import datetime, timedelta

# the now function returns a datetime object
current_date = datetime.now()
print('Today is: ' + str(current_date))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
today = current_date
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

#
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# receive the date as a string and need to convert it to a datetime object
# use strptime function
birthday = input('What is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))