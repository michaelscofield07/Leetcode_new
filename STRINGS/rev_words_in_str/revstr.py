class Solution(object):
    def reverseWords(self, s):
        a=""
        c=""
        for i in s[::-1]:
            if i!=" ":
                c+=i
            else:
                a+=c[::-1]+i
                c=""
        a+=c[::-1]
        return " ".join(a.split())