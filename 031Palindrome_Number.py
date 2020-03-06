class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x >= 0:
            return True
        if x < 0:
            return False
        
        result = 0
        remain = 0
        in_x = x
        while x != 0:
            remain = x % 10
            result = result * 10 + remain
            x = x // 10    # divide without decimal
        
        
        if result != in_x:
            return False
        else:
            return True