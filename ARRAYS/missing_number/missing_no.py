class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s1=n*(n+1)//2
        s2=sum(nums)
        return s1-s2
        """
        :type nums: List[int]
        :rtype: int
        """
        