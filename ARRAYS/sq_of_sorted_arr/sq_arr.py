class Solution(object):
    def sortedSquares(self, nums):
        nums=[i*i for i in nums]
        return sorted(nums)