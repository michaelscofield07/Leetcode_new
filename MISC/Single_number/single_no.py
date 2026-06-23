class Solution(object):
    def singleNumber(self, nums):
        u=0
        for n in nums:
            u^=n
        return u     