class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        L = 0

        for R in range(L+1, len(prices)):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxP = max(profit, maxP)
            else:
                L = R
            R += 1
        return maxP