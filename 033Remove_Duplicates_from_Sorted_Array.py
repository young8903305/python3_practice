# use in-place algorithm
"""
for is faster than while (just a little bit different in this case)
You should always use for loop if the condition is not automatically be checked
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 0
        for index in range(1, len(nums) ):
            if nums[length] != nums[index]:
                length += 1
                nums[length] = nums[index]
        return length + 1