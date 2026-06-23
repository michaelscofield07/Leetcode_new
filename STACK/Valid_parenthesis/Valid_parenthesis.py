class Solution(object):
    def isValid(self, s):
        stack=[]
        for n in s:
            if n=="(" or n=="{" or n=="[":
                stack.append(n)
            else:
                if len(stack)==0:
                    return False
                if (n==")" and stack[-1]!="(") or (n=="}" and stack[-1]!="{") or (n=="]" and stack[-1]!="["):
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        else:
            return False