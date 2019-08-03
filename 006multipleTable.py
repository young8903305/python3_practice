"""
a multiple table of 9x9
(use one while loop)

1*1=1 2*1=2 3*1=3   ...
1*2=2 2*2=4 3*2=6   ...
        .
        .
        .
"""

a=1
b=1
while b<=9:
    print('%d*%d=%d\t' % (a, b, a*b), end='')
    if a<9:
        a+=1
    else:
        print()
        a=1
        b+=1
