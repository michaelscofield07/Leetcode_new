class Solution(object):
    def intersection(self, nums1, nums2):
        a=set()
        for i in nums1:
            if i in nums2:
                a.add(i)
        return list(a)