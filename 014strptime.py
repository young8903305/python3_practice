"""
datetime object, strptime() example
"""
# The datetime module supplies classes for manipulating dates and times.
from datetime import datetime, timedelta

# now() returns a datetime object of now
current_date = datetime.now()
print('Today is: ' + str(current_date))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
today = current_date
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))


# receive the date as a string and need to convert it to a datetime object
# use strptime function
birthday = input('What is your birthday (mm/dd/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%m/%d/%Y')
print('Birthday: ' + str(birthday_date))
