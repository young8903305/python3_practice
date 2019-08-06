"""
print X, triangle, left triangle, right triangle

python doesn't have switch-case statement, can use dictionary, if-elif-else, or Class to implement
"""

option = 0
while 1:
    option = input('choose a figure you want to print\n1) X\n2) triangle\n3) left triangle\n4) right triangle\n')
    if option == '1':   # X
        row = int(input('input your row number:'))
        for i in range(row):
            for j in range(row):
                if j==i or i+j==row-1:
                    print('*', end='')
                else :
                    print(' ', end='')
            print()  # default has '\n', so don't type \n again.
    elif option == '2': # triangle
        row = int(input('input your row number:'))
        for i in range(row):
            for j in range(row):
                if i+j==row-1:
                    star = ''
                    for s in range(2*i+1):
                        star = star+'*'
                    print(star)
                    break
                else:
                    print(' ', end='')
    elif option == '3': # left triangle     
        row = int(input('input your row number:'))
        for i in range(row):
            for j in range(i+1):
                print('*', end='')
            print()
    elif option == '4': # right triangle
        row = int(input('input your row number:'))
        for i in range(row):
            for j in range (row):
                if i+j >= row-1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    else:
        print('have no this option, please re-input, or ctrl+c to leave this program')
        option = 0
    print()
