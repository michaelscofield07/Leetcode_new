class Solution(object):
    def majorityElement(self, nums):
        f=set(nums)
        maxi=0
        c=0
        for i in f:
            if nums.count(i)>maxi:
                maxi=nums.count(i)
                c=i
        return c