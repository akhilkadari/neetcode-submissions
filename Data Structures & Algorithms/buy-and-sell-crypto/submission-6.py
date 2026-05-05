class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[R] > prices[L]:
                profit = prices[R]-prices[L]
                maxP = max(maxP, profit)
            else:
                L=R
            R+=1
        return maxP