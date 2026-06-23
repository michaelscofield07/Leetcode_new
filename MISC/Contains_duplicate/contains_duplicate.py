class Solution(object):
    def containsDuplicate(self, nums):
            n1=len(nums)
            b=set(nums)
            if n1-len(b)>=1:
                return True
            else:
                return False