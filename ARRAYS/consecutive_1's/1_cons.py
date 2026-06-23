class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        p=0
        for i in nums:
            if i==1:
                p+=1
            else:
                c=max(c,p)
                p=0
        c=max(c,p)
        return c