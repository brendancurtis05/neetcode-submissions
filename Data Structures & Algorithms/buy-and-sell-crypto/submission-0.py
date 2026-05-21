class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        [10,1,5,6,7,1]
        l,r = 0,0 -> 10-10 = 0
        r+=1
        l,r = 0,1 -> 1-10 = -9
        l+=1, r+=1 -> 5-1 = 4
        r+=1 ...

        """

        l, r = 0,1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r+=1
        return max_profit



        