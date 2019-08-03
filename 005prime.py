"""
input a positive integer, judge whether it is a prime number
'use Ctrl+c to interrupt the program'
"""

from math import sqrt
while 1:
    is_prime = True
    num = input('input a positive integer: ')
    if str.isdigit(num):
        num = int(num)
        finish = int(sqrt(num))
        for test in range(2, finish + 1):
            if num % test == 0:
                is_prime = False
                break
        if is_prime and num != 1:
            print('%d is prime number' % num)
        else:
            print('%d is not prime number' % num)
    else:
        print('===This input is not a number===')
