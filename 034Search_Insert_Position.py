"""
Binary Search: first, middle, last
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            middle = (first + last) // 2 # whtch out the division
            if target == nums[middle]:
                return middle
            elif nums[middle] > target:
                last = middle - 1
            else:
                first = middle + 1
        return first