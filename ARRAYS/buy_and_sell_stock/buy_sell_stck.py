class Solution(object):
    def maxProfit(self, prices):
        mini,maxi=9999,0
        for p in prices:
            if p<mini:
                mini=p
            profit=p-mini
            if profit>maxi:
                maxi=profit
        return maxi

        """
        :type prices: List[int]
        :rtype: int
        """
        