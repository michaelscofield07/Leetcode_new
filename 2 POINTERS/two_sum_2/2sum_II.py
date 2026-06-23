class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<=j:
            f=numbers[i]+numbers[j]
            if f==target:
                return [i+1,j+1]
            else:
                if f>target:
                    j-=1
                else:
                    i+=1             