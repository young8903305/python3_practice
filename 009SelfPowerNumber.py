"""

Self-Power number: A number is in the length of n. Sum of every digit in the number to the n power equals the number.

input a number represent the length n. Then find Self-Power number.
"""

bit = int(input(
    'Find Self-Power number.\ninput a number to represent the length of number:'))

top = pow(10, bit-1)
buttom = pow(10, bit)
narcissistic_list = []
for num in range (top, buttom):
    result = 0.0
    temp = num
    while temp!=0:
        result+=pow(temp%10, bit)
        # In Python 3, ‘/’ operator does floating point division for both int and float arguments.
        temp = temp // 10
        # The real floor division operator is "//". It returns floor value for both integer and floating point arguments.
    if result == num:
        narcissistic_list.append(num)

for number in narcissistic_list:
    print(number)
