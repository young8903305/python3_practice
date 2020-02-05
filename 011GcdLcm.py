"""
greatest common divisor & least common multiple

in different module

"""

def gcd(a, b):
    if a > b:
        (a,b)
    else:
        (a, b) = (b, a)
    gcd = a % b
    while(gcd > 0):
        a = b
        b = gcd
        gcd = a % b
    return b

def gcd2(a, b):
    return a if b == 0 else gcd2(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm2(a, b):
    return a * b // gcd2(a, b)

a = int(input('input the first number: '))
b = int(input('input the second number: '))
print('GCD: ', gcd(a, b))
print('LCM: ', lcm(a, b))