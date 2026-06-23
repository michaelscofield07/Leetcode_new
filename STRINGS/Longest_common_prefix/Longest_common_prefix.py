class Solution(object):
     def longestCommonPrefix(self, strs):
        mini=float('inf')
        for i in strs:
            if len(i)<mini:
                mini=len(i)
        i=0
        while i<mini:
            for n in strs:
                if n[i]!=strs[0][i]:
                    return n[:i]
            i+=1
        return strs[0][:i]