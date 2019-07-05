"""
input raidus, calculate circumference and area
"""
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

while 1:
    radius = input('input radius: ')
    if is_number(radius):
        radius = float(radius)
        if radius > 0:
            cir = 2 * radius * math.pi
            area = radius * radius * math.pi
            print('circumference: %.1f\narea: %.1f' % (cir, area))
        else:
            print('please a number greater than 0')
    else:
        print('please input a number')