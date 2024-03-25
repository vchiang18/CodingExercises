# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# solution 1 - using pointers, O(n) time complexity. O(1) memory.

class Solution(object):
    def maxProfit(self, prices):
        max_p = 0
        buy, sell = 0, 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[sell] > prices[buy]:
                max_p = max(max_p, profit)
            else:
                buy = sell  # updates pointer to new lowest value
            sell += 1

        return max_p

# soution 2 - with for loop
    def maxProfit(self, prices):
        max_p = 0
        buy = 0

        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_p = max(max_p, profit)
            else:
                buy = sell

        return max_p

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
