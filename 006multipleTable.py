"""
a multiple table of 9x9
(use one while loop)

1*1=1 2*1=2 3*1=3   ...
1*2=2 2*2=4 3*2=6   ...
        .
        .
        .
"""

b=1
a=1
while a<=9:
    print('%d*%d=%d\t' % (b, a, b*a), end='')
    if b<9:
        b+=1
    else:
        print()
        b=1
        a+=1
