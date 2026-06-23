class Solution(object):
    def moveZeroes(self, nums):
        c=0
        while nums.count(0)>0:
            nums.remove(0)
            c+=1
        for i in range(c):
            nums.append(0)
        return nums