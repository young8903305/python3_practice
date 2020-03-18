class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        stair_1 = 1
        stair_2 = 2
        temp = 0
        for _ in range(n-2):
            temp = stair_1
            stair_1 = stair_2
            stair_2 =  temp + stair_1
        return stair_2