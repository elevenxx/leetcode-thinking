"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 参考 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/

        if not prices:
            return 0
        
        n = len(prices)
        # dp[天数][是否持有股票][卖出次数]
        dp = [[[0, 0 ,0], [0, 0, 0]] for i in range(0, n)]

        # 第一天
        dp[0][1][0] = -prices[0]
        dp[0][1][1] = float('-inf')

        for i in range(1, n):
            
            # 没有卖出过
            dp[i][0][0] = 0


            # 当前没有持股，卖出过一次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i-1][1][0] + prices[i], dp[i-1][0][1])


            # 当前没有持股，卖出过两次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i-1][1][1] + prices[i], dp[i-1][0][2])

            # 当前持股，没有卖出过，可能是今天买的股票，可能是之前买的
            dp[i][1][0] = max(dp[i-1][0][0] - prices[i], dp[i-1][1][0])

            # 当前持股，卖出过一次
            dp[i][1][1] = max(dp[i-1][0][1] - prices[i], dp[i-1][1][1])

        # 卖出过0，1，2次的最大收益
        return max(dp[n-1][0][1],dp[n-1][0][2],0)
