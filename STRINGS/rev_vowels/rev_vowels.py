class Solution(object):
    def reverseVowels(self, s):
        a={'a','e','i','o','u','A','E','I','O','U'}
        sl=list(s)
        i=0
        j=len(sl)-1
        while i<j:
            while i<j and sl[i] not in a:
                i+=1
            while i<j and sl[j] not in a:
                j-=1
            sl[i],sl[j]=sl[j],sl[i]
            i+=1
            j-=1
        return ''.join(sl)