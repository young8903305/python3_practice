def try_finally():
    try:
        print('This is a try-finally statement')
    finally:
        print('finally is executed no matter what, and is generally used to release external resources.')


def try_except():
    num_list = [2, 3, 0]
    try:
        print('This is a try-except statement')
        for num in num_list:
            print(f'6/{num} = {int(6/num)}')
    except ZeroDivisionError:
        print('Oops! <Class \'ZeroDivisionError\'> occurred. you divide 0')

def try_except_finally():
    num_list = [2, 3, 0]
    try:
        print('This is a try-except-finally statement')
        for num in num_list:
            print(f'6/{num} = {int(6/num)}')
    except ZeroDivisionError:
        print('Oops! <Class \'ZeroDivisionError\'> occurred. you divide 0')
    finally:
        print('This is the finally statement.')

# Exceptions are raised when corresponding errors occur at run time, but we can forcefully raise it using the keyword raise.
# We can also optionally pass in value to the exception to clarify why that exception was raised.
def try_raise_except():
    try:
        positive_num = int(input('Enter a positive integer: '))
        if positive_num <= 0:
            raise ValueError('That is not a positive number!')
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    try_finally()
    print()
    try_except()
    print()
    try_except_finally()
    print()
    try_raise_except()


