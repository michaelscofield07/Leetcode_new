class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            value=nums[i]
            diff=target-value
            if value not in d:
                d[diff]=i
            else:
                curr_index=i
                prev=d[value]
                return [curr_index,prev]