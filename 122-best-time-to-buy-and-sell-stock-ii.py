class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            profit += tmp if tmp > 0 else 0
        return profit
