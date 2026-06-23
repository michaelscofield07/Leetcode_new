class Solution(object):
    def findNumbers(self, nums):
        c=0
        for n in nums:
            if len(str(n))%2==0:
                c+=1
        return c
