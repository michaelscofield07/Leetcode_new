class Solution(object):
    def isSubsequence(self, s, t):
        i=j=0
        while i<len(t) and j<len(s):
            if t[i]==s[j]:
                i+=1
                j+=1
            else:
                i+=1

        return True if j==len(s) else False