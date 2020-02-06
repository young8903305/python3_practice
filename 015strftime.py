"""
datetime object, strftime() example
The strftime() method returns a string representing date and time using date, time or datetime object.
"""
# The datetime module supplies classes for manipulating dates and times.
from datetime import datetime

# the now function returns a datetime object
current_date = datetime.now()
print('Today is: ' + str(current_date))

# we have to change datetime type into str
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# or we can use strftime() then format its
print('Year: ' + current_date.strftime('%Y') )
print('Month: ' + current_date.strftime('%-m'))
print('Day: ' + current_date.strftime('%-d') )
print('date and time: ' + current_date.strftime('%m/%d/%Y, %H:%M:%S'))

# %m: Month as a zero-padded decimal number
# %-m: Month as a decimal number.
# %d: Day of the month as a zero-padded decimal.
# %-d: Day of the month as a decimal number.
