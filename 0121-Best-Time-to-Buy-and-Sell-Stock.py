class Solution:
    def maxProfitt(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1
        while sell != len(prices):
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit
            if prices[buys] > prices[sell]:
                buy = sell
            else:
                sell += 1
        return max_profit
