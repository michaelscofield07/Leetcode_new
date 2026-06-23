class Solution(object):
    def maximumCount(self, nums):
        c1=0
        c2=0
        for n in nums:
            if n<0 :
                c1+=1
            elif n>0:
                c2+=1
        return max(c1,c2)