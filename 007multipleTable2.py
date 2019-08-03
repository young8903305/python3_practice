"""
a multiple table of 9x9
(use recursive)

1*1=1 2*1=2 3*1=3   ...
1*2=2 2*2=4 3*2=6   ...
        .
        .
        .
"""

def multiple(a, b):
    if b<=9:
        if a<=9:
            print('%d*%d=%d\t' % (a, b, a*b), end='')
            multiple(a+1, b)
        else:
            print()
            a=1
            b+=1
            multiple(a, b)

multiple(1, 1)