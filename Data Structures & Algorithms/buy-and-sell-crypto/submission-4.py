class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = float("-inf")
        L, R = 0, 1

        while R < len(prices):
            if prices[R] < prices[L]:
                L=R
            else:
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)
            R+=1
        return 0 if maxP == float("-inf") else maxP