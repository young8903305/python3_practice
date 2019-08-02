"""
test three number can be a triangle or not
then calculate its perimeter and area
"""
import math

while 1:
    input_string = input('Insert a list of positive integer, separated by space: ')
    tr_list = input_string.split()
    if len(tr_list) == 3:
        a = int(tr_list[0])
        b = int(tr_list[1])
        c = int(tr_list[2])
        if a > 0 and b > 0 and c > 0:
            if (a + b > c) and (b + c > a) and (a + c > b):
                print('perimeter: %.2f' % (a + b + c))
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print('area: %.2f' % (area))
        else:
            print('please insert positive number')
    else:
        print('please insert \"just\" 3 number')