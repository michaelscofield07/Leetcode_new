class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        c=0
        ck=0
        while c<len(g) and ck<len(s):
            if s[ck]>=g[c]:
                c+=1
            ck+=1
        return  c