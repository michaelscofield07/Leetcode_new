class Solution(object):
    def shortestToChar(self, s, c):
        n=len(s)
        left,right,op=[None]*n,[None]*n,[None]*n
        tmp=float('inf')
        for i in range(n):
            if s[i]==c:
                tmp=0
            left[i]=tmp
            tmp+=1
        tmp=float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:
                tmp=0
            right[i]=tmp
            tmp+=1
        for i in range(n):
            op[i]=min(right[i],left[i])
        return op