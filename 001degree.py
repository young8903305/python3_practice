"""
Celsius & Fahrenheit transform
華氏轉攝氏 c = (f-32)/1.8
攝氏轉華氏 f = c * 1.8 + 32
"""

while 1:
    CF = input('Celsius or Fahrenheit?(C/F) ')
    if (CF!='F') and (CF!='C'):
        print('please input C/F')
        continue
    if CF=='F':
        f = float(input('input Fahrenheit degree:'))
        c = (f - 32) / 1.8
        print('%.1fF = %.1fC' % (f, c))
        finish = 1
    elif CF=='C':
        c = float(input('input Celsius degree:'))
        f = c * 1.8 + 32
        print('%.1fC = %.1fF' % (c, f))
        finish = 1
    if finish==1:
        check = input('exit?(y/n)')
        if check=='y':
            break
        else:
            continue