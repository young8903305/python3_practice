"""
Decorators
The most common way that you're going to interact with decorators
is by using decorators as part of your code.

Which means you merely use other people's decorators and seldom create them.

It's still important to see how decorators process in the python code.
"""

# define what things to do when @logger been used
def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper

# the use of @logger
@logger
def sample():
    print('-- Inside sample function')

# run the function 
sample()