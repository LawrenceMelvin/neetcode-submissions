class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_sell = 0
        curr = 0
        for i in range(1,l):
            sell = prices[i] - prices[curr]
            max_sell = max(max_sell, sell)

            if prices[i] < prices[curr]:
                curr = i

        return max_sell