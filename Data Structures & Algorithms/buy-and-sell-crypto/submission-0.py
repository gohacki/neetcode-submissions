class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > res:
                    res = profit
                r += 1
            else:
                l = r
                r += 1
                if r >= len(prices):
                    break
        return res