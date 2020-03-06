class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        if sign == 1 and x > 2**31-1:
            return 0
        if sign == -1 and x < (2**31)*-1:
            return 0

        x = abs(x)
        list_x = list(str(x))
        list_x.reverse()
        output = int(''.join(list_x))
        if sign == 1 and output < 2**31-1:
            return output;
        elif sign == -1 and output < 2**31:
            return -output;
        else:
            return 0