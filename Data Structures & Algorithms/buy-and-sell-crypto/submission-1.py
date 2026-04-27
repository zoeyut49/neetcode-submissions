class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxp = 0
        for i in range(n - 1):
            while i + 1 < n and prices[i + 1] <= prices[i]:
                i += 1
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                maxp = max(maxp, profit)
        return maxp