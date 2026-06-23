class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        v=0
        maxi=0
        while i<j:
            v=min(height[i],height[j])*(j-i)
            if v>maxi:
                maxi=max(maxi,v)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxi