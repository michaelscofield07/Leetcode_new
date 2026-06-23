class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        c=0
        for n in hours:
            if n>=target:
                c+=1
        return c